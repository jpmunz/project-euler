from helpers import test, primes_up_to

def satisfies_goldbach(n, primes):
    s = 1

    while(True):
        p = n - (2 * s**2)

        if p < 2:
            return False

        if p in primes:
            return True

        s += 1


def find_goldbach_counter(upper_bound):
    primes = primes_up_to(upper_bound)

    for n in range(9, upper_bound, 2):
        if n in primes:
            continue

        if not satisfies_goldbach(n, primes):
            return n

primes = primes_up_to(50)
test(satisfies_goldbach(9, primes), True)
test(satisfies_goldbach(27, primes), True)
test(satisfies_goldbach(33, primes), True)


print find_goldbach_counter(10000)
