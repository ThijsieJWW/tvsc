from __future__ import annotations
import sys


def main(argc: int = None, argv: list[str] = None):
    if argc == None or argv == None:
        argv = sys.argv
        argc = argv

    print(f"Arguments: {' '.join(argv)}")
