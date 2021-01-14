import solution


def test_basicTests():
    assert solution.part1("aA") == ""
    assert solution.part1("Aa") == ""
    assert solution.part1("Xx") == ""
    assert solution.part1("aa") == "aa"
    assert solution.part1("aY") == "aY"


def test_basicMultipleTests():
    assert solution.part1("aAaA") == ""
    assert solution.part1("aAaAAa") == ""
    assert solution.part1("aAaABb") == ""
    assert solution.part1("aAbBAa") == ""
    assert solution.part1("aAbbAa") == "bb"


def test_substitutionTests():
    assert solution.part1("abBA") == ""
    assert solution.part1("abCcCcBA") == ""


def test_part1():
    assert solution.part1("dabAcCaCBAcCcaDA") == "dabCBAcaDA"
