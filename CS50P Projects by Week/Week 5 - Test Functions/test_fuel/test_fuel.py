from fuel import convert, gauge
import pytest

def main():
    test_correct()
    test_zero_divison_error()
    test_value_error()
    print(pytest.ExitCode)

def test_correct():
    assert(convert("1/4")) == 25 and gauge(25) == "25%"
    assert(convert("2/4")) == 50 and gauge(50) == "50%"
    assert(convert("0/4")) == 0 and gauge(0) == "E"
    assert(convert("1/100")) == 1 and gauge(1) == "E"
    assert(convert("99/100")) == 99 and gauge(99) == "F"
    assert(convert("100/100")) == 100 and gauge(100) == "F"


def test_zero_divison_error():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("1.5")
    with pytest.raises(ValueError):
        convert("cat/dog")

if __name__ == "__main__":
    main()