from helpers import test, primes_up_to

def is_circular_prime(p, primes):
    digits = str(p)

    while(True):
        digits = digits[1:] + digits[0]

        if digits == str(p):
            return True

        if int(digits) not in primes:
            return False

def count_circular_primes(n):
    circular_primes = []
    primes = primes_up_to(n)

    for prime in primes:
        if is_circular_prime(prime, primes):
            circular_primes.append(prime)

    return len(circular_primes)


primes = primes_up_to(1000)

test(is_circular_prime(2, primes), True)
test(is_circular_prime(197, primes), True)
test(is_circular_prime(43, primes), False)

test(count_circular_primes(100), 13)

print count_circular_primes(10**6)
