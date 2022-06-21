from __future__ import annotations
import logging
import os
import sys
from tvsc import settings, tools, compiler
from tvsc.log import *
import argparse


class Args(argparse.Namespace):
    version: bool | None
    debug: bool | None
    verbose: bool | None
    uupdate: bool | None
    aupdate: bool | None
    files: list[str]


def main():
    """
    Gets called when tvsc is typed in the console.
    this function is the entry point for the compiler.
    """

    argparser = argparse.ArgumentParser(
        settings.name, description="Compiler for tvsl.", add_help=True
    )

    argparser.add_argument(
        "-v",
        "--version",
        action="store_true",
        dest="version",
        help="show version and exit",
    )

    argparser.add_argument(
        "--debug", action="store_true", dest="debug", help="shows debug information"
    )

    argparser.add_argument(
        "--verbose", action="store_true", dest="verbose", help="shows extra information"
    )

    argparser.add_argument("files", nargs="*", help="all the input files")

    argparser.add_argument(
        "--user-update",
        action="store_true",
        dest="uupdate",
        help="updates tvsc to the newest version and exits.",
    )

    argparser.add_argument(
        "--admin-update",
        action="store_true",
        dest="aupdate",
        help="updates tvsc to the newest version if running as admin. and exits.",
    )

    args: Args = argparser.parse_args()
    if args.debug:
        settings.debug = True
        basicConfig(level=logging.DEBUG, format="%(message)s")
    else:
        basicConfig(level=logging.INFO, format="%(message)s")

    if args.verbose:
        settings.verbose = True
    else:
        settings.verbose = False

    if args.version:
        printf("{} {}", settings.name, settings.version)
        return

    elif args.uupdate:
        os.system(f"python -m pip install --upgrade --no-cache-dir tvsc")
        return

    elif args.aupdate:
        if tools.is_admin():
            os.system(f"python -m pip install --upgrade --no-cache-dir tvsc")
        else:
            error("admin privileges required for admin-update")
            return

    else:
        settings.files = args.files
        settings.initialized = True
        try:
            compiler.compile(*settings.files)
        except Exception as e:
            if settings.debug:
                fatal(str(e))
            else:
                error(str(e))
            sys.exit(1)
