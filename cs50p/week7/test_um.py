from um import count


def test_single_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("hello, um, world") == 1
    assert count("um...") == 1


def test_case_insensitivity():
    assert count("UM") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("UM, UM, um!") == 3


def test_words_containing_um():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("instrumentation") == 0
    assert count("umbrella") == 0


def test_multiple_ums():
    assert count("um, hello, um, world") == 2
    assert count("Um? Mum? Is this that album, um, you liked?") == 2
