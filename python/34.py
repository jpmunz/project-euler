from math import factorial
from helpers import test

factorials = dict([(x, factorial(x)) for x in range(10)])

def is_sum_factorials(i):
    factorial_sum = 0

    for digit in str(i):
        factorial_sum += factorials[int(digit)]

    return factorial_sum == i


def find_sum_of_factorials(n):
    sum_of_factorials = []

    for i in range(3, n):

        if is_sum_factorials(i):
            print i
            sum_of_factorials.append(i)

    return sum(sum_of_factorials)

test(is_sum_factorials(145), True)
test(is_sum_factorials(56), False)

print "Sum: %s" % find_sum_of_factorials(10**7)
