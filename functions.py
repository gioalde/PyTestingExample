def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def convert_fahrenheit_to_celsius(fahrenheit):
    if fahrenheit < -459.67:
        raise AssertionError("Temperature cannot be below absolute zero.")
    return multiply(subtract(fahrenheit, 32), 5 / 9)


def factorial(n):
    """
    Computes the factorial of n.
    """
    if n < 0:
        raise ValueError('received negative input')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def count_word_occurrence_in_string(text, word):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function returns 2
    """
    words = text.split()
    return words.count(word)

def count_word_occurrence_in_file(file_name, word):
    """
    Counts how often word appears in file file_name.
    Example: if file contains "one two one two three four"
             and word is "one", then this function returns 2
    """
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()
            count += words.count(word)
    return count

def check_reactor_temperature(temperature_celsius):
    """
    Checks whether temperature is above max_temperature
    and returns a status.
    """
    from reactor import max_temperature
    if temperature_celsius > max_temperature:
        status = 1
    else:
        status = 0
    return status