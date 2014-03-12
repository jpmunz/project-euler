from math import sqrt
from helpers import test

def count_solutions(p):
    expr = lambda b: ((2*b*p) - p**2) / ((2*b) - (2*p))

    solutions = 0
    b = 1

    while(True):
        a = expr(b)

        if b > a:
            break

        if a + b + sqrt(a**2 + b**2) == p:
            solutions += 1

        b += 1

    return solutions


def find_max_solutions(n):
    max_solutions = 0
    max_p_value = 0

    for p in range(3, n + 1):
        solutions = count_solutions(p)

        if solutions > max_solutions:
            max_solutions = solutions
            max_p_value = p

    return max_p_value

test(count_solutions(120),3)


print find_max_solutions(1000)
