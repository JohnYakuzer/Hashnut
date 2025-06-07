#!/usr/bin/env python3

from args_parser import get_parser
from commands import handle_commands

def main():
    parser = get_parser()
    args = parser.parse_args()
    handle_commands(args)

if __name__ == "__main__":
    main()

