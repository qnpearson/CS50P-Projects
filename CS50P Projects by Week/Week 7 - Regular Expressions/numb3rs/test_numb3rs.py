from numb3rs import validate
import pytest

def main():
    test_correct()
    test_out_of_range()
    test_value_error()
    test_wrong_length()

def test_correct():
    assert(validate("1.2.3.4")) == True
    assert(validate("123.255.111.1")) == True

def test_out_of_range():
    assert(validate("1.1.1.256")) == False
    assert(validate("1")) == False

def test_value_error():
    assert(validate("cat")) == False

def test_wrong_length():
    assert(validate("255")) == False

if __name__ == "__main__":
    main()
