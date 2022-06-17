from __future__ import annotations
from . import settings


def printf(s: str, *f: object, **fkw: object) -> None:
    """printf for python"""
    return print(s.format(*f, **fkw))


def info(s: str, *f: object, **fkw: object) -> None:
    return print(f"[ info ]  {s.format(*f, *fkw)}")


def debug(s: str, *f: object, **fkw: object) -> None:
    if settings.debug:
        return print(f"[ debug ] {s.format(*f, **fkw)}")
