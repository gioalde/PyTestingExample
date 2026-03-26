from functions import add, factorial, subtract, multiply
from functions import convert_fahrenheit_to_celsius as f2c
from functions import factorial
from functions import count_word_occurrence_in_string as count_occurrence
from functions import count_word_occurrence_in_file as count_occurrence_in_file
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

def test_count_word_occurrence_in_string():
    text = "one two one two three four"
    assert count_occurrence(text, "one") == 2
    assert count_occurrence(text, "two") == 2
    assert count_occurrence(text, "three") == 1
    assert count_occurrence(text, "four") == 1
    assert count_occurrence(text, "five") == 0

def test_count_word_occurrence_in_file():
    file_name = "test_file.txt"
    with open(file_name, 'w') as f:
        f.write("one two one two three four")
    assert count_occurrence_in_file(file_name, "one") == 2
    assert count_occurrence_in_file(file_name, "two") == 2
    assert count_occurrence_in_file(file_name, "three") == 1
    assert count_occurrence_in_file(file_name, "four") == 1
    assert count_occurrence_in_file(file_name, "five") == 0