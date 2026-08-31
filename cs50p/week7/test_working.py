import pytest
from working import convert


def test_valid_times():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_invalid_hours():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 15 PM")


def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("cat")
