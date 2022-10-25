from seasons import sing_it
from datetime import date, timedelta

def test_1d():
    yesterday = date.today() - timedelta(days=1)
    assert sing_it(yesterday) == "One thousand, four hundred forty minutes"

def test_30d():
    yestermonth = date.today() - timedelta(days=30)
    assert sing_it(yestermonth) == "Forty-three thousand, two hundred minutes"