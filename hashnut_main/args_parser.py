import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="Hashnut - File Hashing CLI Tool", add_help=False)
    parser.add_argument("paths", nargs="*", help="Path to file(s)")
    parser.add_argument("-p", action="store_true", help="Output hash to .txt file")
    parser.add_argument("-c", action="store_true", help="Compare two files")
    parser.add_argument("-sha1", action="store_true", help="Use SHA-1")
    parser.add_argument("-sha256", action="store_true", help="Use SHA-256")
    parser.add_argument("-sha512", action="store_true", help="Use SHA-512")
    parser.add_argument("-md5", action="store_true", help="Use MD5")
    parser.add_argument("-blake2b", action="store_true", help="Use BLAKE2b")
    parser.add_argument("-sha3_256", action="store_true", help="Use SHA3-256")
    parser.add_argument("-en", action="store_true", help="Encrypt file")
    parser.add_argument("-de", action="store_true", help="Decrypt file")
    parser.add_argument("--about", action="store_true", help="About the author")
    parser.add_argument("-h", "--help", action="help", help="Show this help message and exit")
    return parser

