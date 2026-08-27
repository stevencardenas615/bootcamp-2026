from plates import is_valid

def test_punctuation():
    assert is_valid("P13.14") == False
    assert is_valid("CS.50") == False
    assert is_valid("AB") == True

def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("AB20") == True

def test_starts_with_letters():
    assert is_valid("AB") == True
    assert is_valid("CS50") == True
    assert is_valid("+A") == False
    assert is_valid("A1") == False
    assert is_valid("aa") == True

def test_end_with_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_first_number():
    assert is_valid("AAA022") == False
    assert is_valid("AAA222") == True
