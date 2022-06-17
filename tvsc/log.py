from __future__ import annotations
from . import settings


def printf(s: str, *f: object, **fkw: object) -> None:
    """printf for python"""
    return print(s.format(*f, **fkw))


def info(s: str, *f: object, **fkw: object) -> None:
    return print(f"{settings.name}: {s.format(*f, *fkw)}")


def error(s: str, *f: object, **fkw: object) -> None:
    return print(f"{settings.name}: fatal: {s.format(*f, *fkw)}")


def debug(s: str, *f: object, **fkw: object) -> None:
    if settings.debug:
        return print(f"{settings.name}: debug: {s.format(*f, **fkw)}")


def verbose(s: str, *f: object, **fkw: object) -> None:
    if settings.verbose:
        return print(f"{settings.name}: verbose: {s.format(*f, **fkw)}")
