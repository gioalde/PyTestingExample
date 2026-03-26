from functions import add, factorial, subtract, multiply
from functions import convert_fahrenheit_to_celsius as f2c
from functions import factorial
import pytest


def test_add():
    assert add(2, 3) == 5
    assert add("space", "ship") == "spaceship"


def test_subtract():
   assert subtract(3,2) == 1


def test_convert_fahrenheit_to_celsius():
   assert f2c(32) == 0
   assert f2c(122) == pytest.approx(50)
   with pytest.raises(AssertionError):
       f2c(-600)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2

    