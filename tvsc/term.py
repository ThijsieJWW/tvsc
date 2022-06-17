from __future__ import annotations
from tvsc import settings
from tvsc.log import *
import argparse


class Args(argparse.Namespace):
    version: bool | None
    debug: bool | None


def main():
    argparser = argparse.ArgumentParser(
        settings.name, description="Compiler for tvsl.", add_help=True
    )

    argparser.add_argument("-v", "--version", action="store_true", dest="version")
    argparser.add_argument("--debug", action="store_true", dest="debug")

    args: Args = argparser.parse_args()
    if args.debug:
        settings.debug = True
    else:
        settings.debug = False

    if args.version:
        printf("%(name)s %(version)s", name=settings.name, version=settings.version)

    settings.initialized = True
