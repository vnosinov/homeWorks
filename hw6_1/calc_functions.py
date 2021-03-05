# file with functions for the calculator
def c_sum(a, b):
    """
    the sum of to numbers
    :param a: number 1
    :param b: number 2
    :return: sum
    """
    return a + b


def c_diff(a, b):
    """
    difference of two numbers
    :param a: number 1
    :param b: number 2
    :return: diff
    """
    return a - b


def c_mult(a, b):
    """
    multiplication of two numbers
    :param a: number 1
    :param b: number 2
    :return: multiplication
    """
    return a * b


def c_div(a, b):
    """
    division of two numbers
    :param a: number 1
    :param b: number 2
    :return: division
    """
    if b == 0:
        return print('division by nul')
    return a / b
