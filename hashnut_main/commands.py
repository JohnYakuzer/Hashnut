from utils import (
    calculate_hash,
    write_hashes_to_file,
    compare_files,
    encrypt_file,
    decrypt_file,
    SUPPORTED_ALGOS,
    log_action
)

def handle_commands(args):
    selected_algos = [algo for algo in SUPPORTED_ALGOS if getattr(args, algo)]

    if args.about:
        print("Hashnut v1.0\nAuthor: John Yakuzer\nSecure & simple file hashing utility.")
        log_action("Displayed about info")
        return

    if args.c:
        if len(args.paths) < 2:
            print("[ERROR] You must provide two files for comparison.")
            return
        h1, h2 = compare_files(args.paths[0], args.paths[1], selected_algos)
        if args.p:
            write_hashes_to_file(args.paths[0], h1)
            write_hashes_to_file(args.paths[1], h2)
    elif args.en:
        if not args.paths:
            print("[ERROR] Provide a file to encrypt.")
            return
        encrypt_file(args.paths[0], selected_algos[0] if selected_algos else "sha256")
    elif args.de:
        if not args.paths:
            print("[ERROR] Provide a file to decrypt.")
            return
        decrypt_file(args.paths[0], selected_algos[0] if selected_algos else "sha256")
    else:
        if len(args.paths) < 1:
            print("[ERROR] No file provided.")
            return
        hashes = calculate_hash(args.paths[0], selected_algos)
        for k, v in hashes.items():
            print(f"{k.upper()}: {v}")
        if args.p:
            write_hashes_to_file(args.paths[0], hashes)

