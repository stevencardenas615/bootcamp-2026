from datetime import date
from seasons import get_minutes

def test_one_year():
    birth = date(2021, 1, 1)
    today = date(2022, 1, 1)

    assert get_minutes(birth, today) == "Five hundred twenty-five thousand, six hundred minutes"

def test_two_years():
    birth = date(2018, 1, 1)
    today = date(2020, 1, 1)

    assert get_minutes(birth, today) == "One million, fifty-one thousand, two hundred minutes"

def test_leap_year():
    birth = date(2020, 1, 1)
    today = date(2021, 1, 1)

    assert get_minutes(birth, today) == "Five hundred twenty-seven thousand forty minutes"
