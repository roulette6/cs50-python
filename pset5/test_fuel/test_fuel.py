from fuel import convert, gauge
import pytest


def test_convert_half():
    assert convert("1/2") == 50


def test_convert_80():
    assert convert("4/5") == 80


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_larger_numerator():
    with pytest.raises(ValueError):
        convert("2/1")


def test_gauge_1():
    assert gauge(1) == "E"


def test_gauge_50():
    assert gauge(50) == "50%"


def test_gauge_99():
    assert gauge(99) == "F"
