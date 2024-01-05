from jar import Jar
import pytest


def test_init():
    test_str()
    test_deposit()
    test_withdraw()
    test_capacity()


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"


def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_capacity():
    jar = Jar(3)
    with pytest.raises(ValueError):
        jar.deposit(4)