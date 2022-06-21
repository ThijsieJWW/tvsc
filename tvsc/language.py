"""
Here are al the regexes for the compiler. Maybe there will be more languages from tvsc.
"""

tvsl = [
    ("lang \w+;", "__LANG_DECL__"),
    ("\d+", "NUMBER"),
    ("[a-zA-Z_]\w+", "IDENTIFIER"),
    ("\/\/[^\n]*", "COMMENT"),
]


def get_lang(filecontent: str) -> list[tuple[str, str]]:
    l = filecontent.splitlines()
    if len(l) < 1:
        raise Exception(
            f"syntax error: language declaration must be at the top of the file."
        )
    else:
        l = l[0]
    ls = l.split(" ")
    if ls[0] == "lang":
        if len(ls) >= 2:
            if ls[1].lower() in ["'tvsl';", '"tvsl";']:
                return tvsl
            else:
                raise Exception(f"language `{ls[1]}` is not available for tvsc.")
        else:
            raise Exception(
                f"syntax error: language declaration must be at the top of the file."
            )
    else:
        raise Exception(
            f"syntax error: language declaration must be at the top of the file."
        )
