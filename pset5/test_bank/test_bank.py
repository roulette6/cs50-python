from bank import value

def test_value_hello_lower():
    assert value("hello") == 0

def test_value_hello_upper():
    assert value("HELLO") == 0

def test_value_hi_lower():
    assert value("hi") == 20

def test_value_hi_upper():
    assert value("HI") == 20

def test_value_wassup_lower():
    assert value("wassup") == 100

def test_value_wassup_upper():
    assert value("WASSUP") == 100