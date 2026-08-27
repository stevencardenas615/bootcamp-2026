import pytest
from bank import value

def test_value():
    assert value("hello") == 0
    assert value("how are you?") == 20
    assert value("whats up!") == 100

def test_case():
    assert value("HELLO") == 0
