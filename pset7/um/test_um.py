from um import count


def test_one_lower():
    assert count("um") == 1


def test_one_upper():
    assert count("Um") == 1


def test_one_punct():
    assert count("um?") == 1


def test_one_punct_one_sub():
    assert count("Um, thanks for the album.") == 1


def test_two_sub():
    assert count("A drum has two sums.") == 0


def test_two_punct2():
    assert count("Um, thanks, um...") == 2
