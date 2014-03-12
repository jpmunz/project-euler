from math import sqrt
from itertools import permutations

def test(actual, expected):
    assert expected == actual, "Expecting %s, got %s" % (expected, actual)

prime_set = set([2])
composite_set = set([])

def divisors(n):
    """Returns the divisors of n"""
    return [x for x in range(1, (n/2) + 1) if n % x == 0] + [n]

def is_prime_divisors(n):
    num_divisors = 1
    x = 1
    while(x < (n/2) + 1):
        if n % x == 0:
            num_divisors += 1

        if num_divisors > 2:
            return False

        x += 1

    return True

def is_palindrome(n):
    """Tests whether n is a palindrome"""
    s = str(n)
    return s == s[::-1]

def fib_up_to(val):
    """Returns the fibonacci sequence for terms up to val"""
    result = [1, 2]
    while True:
        next = result[-1] + result[-2]
        if next > val: break
        result.append(next)

    return result

def primes(n):
    """Returns the first n primes"""
    result = []
    x = 2
    while True:
        if is_prime(x): result.append(x)
        if len(result) == n: break
        x += 1
    return result

def primes_up_to(val):
    """Returns the primes up to val"""
    for i in range(3, val + 1, 2):
        if not i in composite_set:
            prime_set.add(i)

            if i <= sqrt(val):
                for c in range(i**2, val + 1, 2 * i):
                    composite_set.add(c)

    return prime_set

def is_prime(n, cache_result=True):
    """Tests whether n is prime"""
    if not (n in prime_set or n in composite_set):
        if is_prime_divisors(n):
            if not cache_result:
                return True

            prime_set.add(n)
        else:
            if not cache_result:
                return False
            composite_set.add(n)

    return n in prime_set

def prime_factors(n, distinct=False):
    """Returns the prime factors of n"""

    factors = set([]) if distinct else []

    d = 2
    while(True):
        if n == 1:
            return factors

        if n % d == 0:
            n /= d

            if distinct:
                factors.add(d)
            else:
                factors.append(d)
        else:
            if d == 2:
                d += 1
            else:
                d += 2


def is_pandigital(n):
    digits = str(n)

    if len(digits) != 9:
        return False

    found = set([])
    for digit in digits:
        if digit in found or digit == '0':
            return False
        else:
            found.add(digit)

    return True

def triangle_number(n):
    return (.5 * n)*(n + 1)

def pentagonal_number(n):
    return (n * (3*n - 1)) / 2.0

def hexagonal_number(n):
    return (n * (2*n - 1))

def is_triangle_number(tn):
    n = (-1 + sqrt(1 + (8*tn))) / 2
    return int(n) == n

def is_pentagonal_number(pn):
    n = (1 + sqrt(1 + (24*pn))) / 6
    return int(n) == n

def is_hexagonal_number(hn):
    n = (1 + sqrt(1 + (8*hn))) / 4
    return int(n) == n

def permutate_number(n):
    return set([int(''.join(perm)) for perm in permutations(str(n))])



