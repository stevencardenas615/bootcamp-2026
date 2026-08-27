import fuel
import pytest

def test_valid_converts():
    assert fuel.convert("1/4") == 25
    assert fuel.convert("4/4") == 100
    assert fuel.convert("0/1") == 0

def test_invalid_converts():
    with pytest.raises(ValueError):
        fuel.convert("-1/4")
    with pytest.raises(ValueError):
        fuel.convert("5/4")
    with pytest.raises(ValueError):
        fuel.convert("cat/dog")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")

def test_gauge():
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(25) == "25%"
    assert fuel.gauge(75) == "75%"
