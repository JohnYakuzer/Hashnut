# Hashnut

Hashnut is a command-line tool for hashing, comparing, encrypting, and decrypting files. It supports multiple hash algorithms and provides a simple, efficient interface for file integrity verification and basic file encryption.

---

## Features

- Compute file hashes using MD5, SHA-1, SHA-256, SHA-512, BLAKE2b, SHA3-256
- Compare hashes of two files
- Encrypt and decrypt files
- Export hash outputs to `.txt` files
- Easy-to-use command-line interface

---

## Requirements

- Python 3.x
- `cryptography` package (version >= 42.0.5)

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Installation Linux

- Clone the repo
```bash
git clone https://github.com/JohnYakuzer/Hashnut.git
cd hashnut/hashnut_main
```

- Perform `chmod`
```bash
chmod +x hashnut install.sh
```

- Run the command for more info
```bash
hashnut --help
```

---

## Installation Windows

- Clone the repo
```bash
git clone https://github.com/JohnYakuzer/Hashnut.git
cd hashnut/hashnut_main
```

- Run the provided PowerShell install script:
```bash
./win_install.ps1
```

- This script will copy `hashnut.bat` to `%USERPROFILE%\bin` and add that directory to your User PATH environment variable.

- Restart your terminal or log off/on to apply the PATH changes.

- Run the command for more info
```bash
hashnut --help
```
