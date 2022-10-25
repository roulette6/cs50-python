from response import validate


def test_valid_com():
    assert validate("dude@dude.com") == "Valid"


def test_valid_edu():
    assert validate("dude@dude.edu") == "Valid"


def test_no_at():
    assert validate("dude") == "Invalid"


def test_multiple_at():
    assert validate("dude@@@dude.com") == "Invalid"


def test_no_subdomain():
    assert validate("dude@com") == "Invalid"


def test_consecutive_dots():
    assert validate("dude@dude..com") == "Invalid"
