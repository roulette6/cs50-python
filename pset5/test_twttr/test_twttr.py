from twttr import shorten

def test_shorten_lowercase():
    assert shorten("alfalfa") == "lflf"

def test_shorten_uppercase():
    assert shorten("ALBONDIGA") == "LBNDG"

def test_shorten_spaces():
    assert shorten("a meat wad") == " mt wd"

def test_shorten_numbers():
    assert shorten("abc123") == "bc123"

def test_shorten_punct():
    assert shorten("I am.") == " m."