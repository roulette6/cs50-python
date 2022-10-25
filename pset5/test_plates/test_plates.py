from plates import is_valid


def test_is_valid_start_num():
    assert is_valid("55") == False


def test_is_valid_too_long():
    assert is_valid("ABCDEFG1234") == False


def test_is_valid_punctuation():
    assert is_valid("AB1.,5") == False


def test_is_valid_middle_numbers():
    assert is_valid("AB12GD") == False


def test_is_valid_leading_zero():
    assert is_valid("AB0") == False


def test_is_valid_spaces():
    assert is_valid("AB C5") == False


def test_is_valid_good_input():
    assert is_valid("ABC45") == True
