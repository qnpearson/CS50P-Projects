import pytest
from seasons import sing, convert

def main():
    test_correct()
    test_invalid_date()
    #test_invalid_format()

def test_correct():
    assert(sing(convert("1999", "01", "01"))) == "Twelve million, nine hundred seventy-seven thousand, two hundred eighty minutes"

def test_invalid_date():
    with pytest.raises(ValueError):
        sing(convert("February", "9th", "1909"))
"""def test_invalid_format():
    ..."""

if __name__ == "__main__":
    main()