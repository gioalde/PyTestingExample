def FizzBuzz(n):
    '''FizzBuzz - i.e. a function that:

    takes an integer argument

    for arguments that are multiples of three, returns “Fizz”

    for arguments that are multiples of five, returns “Buzz”

    for arguments that are multiples of both three and five, returns “FizzBuzz”

    fails in case of non-integer arguments or integer arguments 0 or negative

    otherwise returns the integer itself'''

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n <= 0:
        raise ValueError("Input must be a positive integer")

    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n