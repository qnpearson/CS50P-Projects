import pytest

from working import convert

def main():
    test_check_spaces()
    test_check_to()
    test_check_minutes()

def test_check_spaces():
    assert(convert("9 AM to 5 PM")) == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert("9AM to 5PM")

def test_check_to():
    assert(convert("10 AM to 6 PM")) == "10:00 to 18:00"
    with pytest.raises(ValueError):
        convert("10 AM - 6 PM")

def test_check_minutes():
    assert(convert("10:30 AM to 6:30 PM")) == "10:30 to 18:30"
    with pytest.raises(ValueError):
        convert("10:60 AM to 6:61 PM")

if __name__ == "__main__":
    main()