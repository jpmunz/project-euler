from helpers import test, primes_up_to

def is_truncatable_prime(p, primes):
    digits = str(p)

    if len(digits) == 1:
        return False

    left_truncation = lambda digits: digits[1:]
    right_truncation = lambda digits: digits[:-1]

    for truncate in [left_truncation, right_truncation]:

        remaining_digits = digits
        while(True):
            remaining_digits = truncate(remaining_digits)

            if len(remaining_digits) == 0:
                break

            if not int(remaining_digits) in primes:
                return False

    return True

def find_truncatable_primes():
    truncatable_primes = set([])

    n = 100
    while(True):
        primes = primes_up_to(n)

        for p in primes:
            if is_truncatable_prime(p, primes):
                truncatable_primes.add(p)

                if len(truncatable_primes) == 11:
                    return truncatable_primes
        n *= 10

primes = primes_up_to(10000)

test(is_truncatable_prime(3797, primes), True)
test(is_truncatable_prime(37, primes), True)
test(is_truncatable_prime(2, primes), False)
test(is_truncatable_prime(43, primes), False)

print sum(find_truncatable_primes())
