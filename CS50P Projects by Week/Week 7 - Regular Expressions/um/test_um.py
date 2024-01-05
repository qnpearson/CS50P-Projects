from um import count
import pytest

def main():
    test_space()
    test_punctuation()
    test_caps()
    test_ums()
    test_umms()

def test_space():
    assert(count( "um ")) == 1
    assert(count( " um")) == 1

def test_punctuation():
    assert(count("um...")) == 1
    assert(count("...um...")) == 1

def test_caps():
    assert(count("UM")) == 1

def test_ums():
    assert(count("um um")) == 2

def test_umms():
    assert(count("umm")) == 0

if __name__ == "__main__":
    main()