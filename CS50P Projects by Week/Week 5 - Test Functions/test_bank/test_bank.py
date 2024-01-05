from bank import value

#Call Test Functions
def main():
    value_hello()
    value_h()
    value_no_h()

def test_value_hello():
    assert value("hello") == 0
    assert value("hello how are you?") == 0
    assert value("heLlo") == 0
    #assert value("h") == 0

def test_value_h():
    assert value("h") == 20
    assert value("hi how are you?") == 20
    assert value("Hi") == 20

def test_value_no_h():
    assert value("good afternoon") == 100
    assert value("goOd aftErnoon") == 100

if __name__ == "__main__":
    main()