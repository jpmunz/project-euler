from fractions import Fraction
from helpers import test


def expand_root(n):
    last_denominator = 0

    while(True):
        denominator = Fraction(1, n + last_denominator)
        yield Fraction(1 + denominator)
        last_denominator = denominator

def find_greater_numerator_digits(upper_bound):
    count = 0

    for i, expansion in enumerate(expand_root(2)):
        if i >= upper_bound:
            return count

        if len(str(expansion.numerator)) > len(str(expansion.denominator)):
            count += 1

expander = expand_root(2)
test(expander.next(), Fraction(3, 2))
test(expander.next(), Fraction(7, 5))

print find_greater_numerator_digits(1000)
