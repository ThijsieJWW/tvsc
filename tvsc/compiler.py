from . import log
from . import lexer, language


def compile(*files: str) -> None:
    if len(files) < 1:
        raise Exception("no input file provided.")
    else:
        log.debug(f"input files: {', '.join(files)}")

    lxs: dict[str, lexer.Lexer] = {}
    for f in files:
        try:
            fp = open(f)
            fc = fp.read()
            lxs[f] = lexer.Lexer(language.get_lang(fc))
            lxs[f].input(fc)
        except FileNotFoundError:
            raise Exception(f"cannot open file `{f}`.")
        finally:
            fp.close()

    for i in lxs:
        print(f"FILE: {i}")
        for tok in lxs[i].tokens():
            print(tok)
