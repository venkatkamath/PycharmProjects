import sys


def is_prime(number):
    if number <= 1:
        return False
    for x in xrange(2, number):
        if number % x == 0:
            return False
    return True


def next_prime(number):
    for x in xrange(number+1, sys.maxsize):
        if is_prime(x):
            return x
