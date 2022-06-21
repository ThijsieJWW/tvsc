from __future__ import annotations
from sys import stderr
from . import settings
from logging import basicConfig, exception
import colorama

colorama.init(autoreset=True)


def printf(s: str, *f: object, **fkw: object) -> None:
    """printf for python"""
    return print(s.format(*f, **fkw))


def info(s: str, *f: object, **fkw: object) -> None:
    return print(f"{settings.name}: {s.format(*f, *fkw)}")


def fatal(s: str, *f: object, **fkw: object) -> None:
    return exception(
        f"{colorama.Fore.RED}{settings.name}: fatal:{colorama.Fore.RESET} {s.format(*f, *fkw)}",
    )


def error(s: str, *f: object, **fkw: object) -> None:
    return print(
        f"{colorama.Fore.RED}{settings.name}: error:{colorama.Fore.RESET} {s.format(*f, *fkw)}",
        file=stderr,
    )


def debug(s: str, *f: object, **fkw: object) -> None:
    if settings.debug:
        return print(f"{settings.name}: debug: {s.format(*f, **fkw)}")


def verbose(s: str, *f: object, **fkw: object) -> None:
    if settings.verbose:
        return print(f"{settings.name}: verbose: {s.format(*f, **fkw)}")
