from itertools import permutations
from helpers import primes_up_to

def find_largest_pandigital_prime(n_digits):

    primes = primes_up_to(10**n_digits)
    digits = [str(d) for d in range(1, n_digits + 1)]

    while(digits):
        max_found = 0

        for arrangement in permutations(digits):
            n = int(''.join(arrangement))

            if n in primes:
                max_found = max(n, max_found)

        if max_found:
            return max_found

        digits.pop()


print find_largest_pandigital_prime(7)
