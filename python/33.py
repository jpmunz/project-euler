from fractions import Fraction

from helpers import test


def is_curious_fraction(n, d):
    n1 = n / 10
    n2 = n % 10
    d1 = d / 10
    d2 = d % 10

    # ignore trivial cases
    if n2 == 0 or d2 == 0:
        return False

    fraction = n / float(d)
    return n2 == d1 and n1/float(d2) == fraction and fraction < 1


def find_curious_fractions():
    curious_fractions = []

    for num in range(10**1, 10**2):
        for denom in range(10**1, 10**2):
            if is_curious_fraction(num, denom):
                print "%s / %s" % (num, denom)
                curious_fractions.append(Fraction(num, denom))

    return curious_fractions


test(is_curious_fraction(49, 98), True)
test(is_curious_fraction(30, 50), False)
test(is_curious_fraction(31, 15), False)
test(is_curious_fraction(11, 11), False)

fractions = find_curious_fractions()

# Find the denominator of the product of the fractions
print reduce(lambda a, b: a*b, fractions).denominator
