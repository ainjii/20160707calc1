def add(num1, num2):
    """Returns the sum of two numbers.

    Adds num1 to num2 and returns the result.
    """
    return num1 + num2

def subtract(num1, num2):
    """Subtracts two numbers.

    Subtracts num2 from num1 and returns the result.
    """
    return num1 - num2

def multiply(num1, num2):
    """Multiplies two numbers.

    Multiplies num1 and num2, and returns the result.
    """
    return num1 * num2

def divide(num1, num2):
    """Divides two numbers.

    Divides num1 by num2 and returns the result as a float.
    """
    return float(num1)/float(num2)

def square(num1):
    """Squares the number.

    Multiplies a number by itself
    """
    return num1*num1

def cube(num1):
    """Cubes a number.

    Multiples a number by itself three times
    """
    return num1**3

def power(num1, num2):
    """Raises a number by the power of the second number.

    Num1 is raised by the power of num2.
    """
    return num1**num2

def mod(num1, num2):
    """Divides a number by another number and returns the remainder.

    Divides num1 by num2 and returns the remainder.
    """
    return num1%num2
