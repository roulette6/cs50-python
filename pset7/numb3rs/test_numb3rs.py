from numb3rs import validate


def test_invalid_first():
    assert validate("256.3.6.8") == False


def test_invalid_second():
    assert validate("1.300.6.8") == False


def test_ipv6():
    assert validate("2001:db8:3333:4444:5555:6666:7777:8888") == False


def test_invalid_input():
    assert validate("cat") == False


def test_loopback():
    assert validate("127.0.0.1") == True


def test_broadcast():
    assert validate("255.255.255.255") == True
