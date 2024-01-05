import pytest
from plates import is_valid

def main():
    test_alpha()
    test_correct()
    test_first_num()
    test_length()
    test_zero_first()
    test_number_first()
    #print(pytest.ExitCode)

def test_alpha():
    assert(is_valid("!CS50")) == False
    assert(is_valid("CS50!")) == False


def test_correct():
    assert(is_valid("CS50")) == True
    assert(is_valid("AB55")) == True

def test_first_num():
    assert(is_valid("1CS50")) == False

def test_length():
    assert(is_valid("CS50000")) == False

def test_zero_first():
    assert(is_valid("CS01")) == False

def test_number_first():
    #assert(is_valid("0SCS50")) == False
    assert(is_valid("CS50A")) == False


if __name__ == "__main__":
    main()

