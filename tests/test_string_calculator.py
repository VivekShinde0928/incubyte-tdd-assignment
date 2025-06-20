from src.string_calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number():
    assert add("4") == 4

def test_two_numbers():
    assert add("1,2") == 3

def test_two_numbers_delimeter():
    assert add("1\n2,3") == 6


def test_different_delimeter():
    assert add("//;\n1;2") == 3