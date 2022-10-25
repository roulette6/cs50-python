from jar import Jar
import pytest


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10


def test_str():
    jar = Jar(10)
    jar.deposit(7)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.deposit(5)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(3)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.withdraw(8)
