# Joshua Hamaker        04/16/25
# Boolean Equalence Practice


class BoolEquivilanceException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return "ERROR: Expressions not equvielant"


def main() -> None:
    bools = [True, False]
    print("testing 'and'")
    for i in bools:
        for j in bools:
            if altAnd(i, j) != (i and j):
                raise BoolEquivilanceException
    print("'and' successful\ntesting 'or'")
    for i in bools:
        for j in bools:
            if altOr(i, j) != (i or j):
                raise BoolEquivilanceException
    print("'or' successful\ntesting 'and not'")
    for i in bools:
        for j in bools:
            if altAndNot(i, j) != (i and not j):
                raise BoolEquivilanceException
    print("'and not' successful\ntesting 'just b'")
    for i in bools:
        for j in bools:
            if altJustB(i, j) != j:
                raise BoolEquivilanceException
    print("'just b' successful")


def altAnd(a: bool, b: bool) -> bool:
    if a:
        if b:
            return True
    return False


def altOr(a: bool, b: bool) -> bool:
    if a:
        return True
    if b:
        return True
    return False


def altAndNot(a: bool, b: bool) -> bool:
    ans = False
    if a:
        ans = True
    if b:
        ans = False
    return ans


def altJustB(a: bool, b: bool) -> bool:
    ans = False
    if a:
        ans = False
    if b:
        ans = True
    return ans


if __name__ == '__main__':
    main()