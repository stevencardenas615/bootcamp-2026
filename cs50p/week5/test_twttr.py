import pytest
from twttr import shorten

def test_vowels():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Apple") == "ppl"
    assert shorten("Number") == "Nmbr"

def test_numbers():
    assert shorten("123") == "123"
    assert shorten("I have 2 apples") == " hv 2 ppls"

def test_punctuation():
    assert shorten("@Twitter") == "@Twttr"
    assert shorten("Apple!") == "ppl!"
