from numb3rs import validate

def test_valid_ip():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.1.1") == True

def test_invalid_range():
    assert validate("256.100.100.100") == False
    assert validate("100.256.100.100") == False
    assert validate("100.100.256.100") == False
    assert validate("100.100.100.256") == False
    assert validate("512.512.512.512") == False

def test_invalid_format():
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1") == False

    assert validate("cat") == False
    assert validate("1.2.3.cat") == False
    assert validate("cs50.com") == False

def test_invalid_punc():
    assert validate("192,168,1,1") == False
    assert validate("192..168.1.1") == False
