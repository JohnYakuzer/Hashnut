import hashlib
import os
from datetime import datetime
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import secrets
import getpass

LOG_PATH = "hashnut.log"

SUPPORTED_ALGOS = {
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha256': hashlib.sha256,
    'sha512': hashlib.sha512,
    'blake2b': hashlib.blake2b,
    'sha3_256': hashlib.sha3_256,
}

def log_action(action: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, 'a') as f:
        f.write(f"[{timestamp}] {action}\n")

def calculate_hash(file_path, algorithms):
    results = {}
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
            for name, algo in SUPPORTED_ALGOS.items():
                if not algorithms or name in algorithms:
                    hash_obj = algo()
                    hash_obj.update(data)
                    results[name] = hash_obj.hexdigest()
        log_action(f"Calculated hashes for {file_path}")
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        log_action(f"Failed to find file: {file_path}")
    return results

def write_hashes_to_file(file_path, hashes, output_path=None):
    fname = os.path.basename(file_path)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output = output_path or f"{file_path}_hash.txt"

    with open(output, 'w') as f:
        f.write(f"Hash Report for: {fname}\nGenerated: {now}\n")
        f.write("=" * 50 + "\n")
        for name, value in hashes.items():
            f.write(f"{name.upper()}: {value}\n")
    print(f"[+] Hash output saved to: {output}")
    log_action(f"Saved hash report to {output}")

def compare_files(file1, file2, algorithms):
    h1 = calculate_hash(file1, algorithms)
    h2 = calculate_hash(file2, algorithms)

    print(f"Comparing:\n  {file1}\n  {file2}\n")
    for algo in h1:
        result = "MATCH" if h1[algo] == h2[algo] else "DIFFER"
        print(f"{algo.upper():<10}: {result}")
    log_action(f"Compared {file1} and {file2}")
    return h1, h2

def derive_key_from_password(password: str, algo_name="sha256") -> bytes:
    if algo_name not in SUPPORTED_ALGOS:
        raise ValueError("Unsupported hash for key derivation.")
    digest = SUPPORTED_ALGOS[algo_name]()
    digest.update(password.encode())
    return digest.digest()[:32]

def encrypt_file(file_path, algo="sha256"):
    password = getpass.getpass("Enter password for encryption: ")
    key = derive_key_from_password(password, algo)
    aesgcm = AESGCM(key)
    nonce = secrets.token_bytes(12)

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted = aesgcm.encrypt(nonce, data, None)
    with open(file_path + ".enc", "wb") as f:
        f.write(nonce + encrypted)

    print(f"[+] Encrypted: {file_path}.enc")
    log_action(f"Encrypted file {file_path}")

def decrypt_file(file_path, algo="sha256"):
    password = getpass.getpass("Enter password for decryption: ")
    key = derive_key_from_password(password, algo)
    aesgcm = AESGCM(key)

    with open(file_path, "rb") as f:
        nonce = f.read(12)
        ciphertext = f.read()

    try:
        decrypted = aesgcm.decrypt(nonce, ciphertext, None)
    except Exception as e:
        print("[!] Decryption failed:", str(e))
        log_action(f"Failed to decrypt file {file_path}")
        return

    output_path = file_path.replace(".enc", "") + "_decrypted"
    with open(output_path, "wb") as f:
        f.write(decrypted)

    print(f"[+] Decrypted: {output_path}")
    log_action(f"Decrypted file {file_path}")

