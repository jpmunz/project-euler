from math import factorial
from helpers import test

def ways(n, r):
    diff = n - r
    cancel = max(diff, r)

    numerator = reduce(lambda a, b: a*b, [1] + range(cancel + 1, n + 1))
    denominator = factorial(min(diff, r))

    return numerator / denominator

def ways_greater_than(value, n_upper_bound):
    ways_greater = 0

    for n in range(1, n_upper_bound + 1):
        for r in range(1, n + 1):
            if ways(n, r) > value:
                ways_greater += 1

    return ways_greater

test(ways(23, 10), 1144066)
test(ways(10, 10), 1)

print ways_greater_than(1000000, 100)
