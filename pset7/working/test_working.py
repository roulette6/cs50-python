from working import convert
import pytest


def test_hh_am():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_12_am_12_pm():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_12_pm_12_am():
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_hh_mm_am():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_hh_pm():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_hh_mm_pm():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_invalid_mm():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_invalid_hh():
    with pytest.raises(ValueError):
        convert("9:00 AM - 17:00 PM")


def test_invalid_separator():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


def test_missing_meridiem ():
    with pytest.raises(ValueError):
        convert("9 to 5")
