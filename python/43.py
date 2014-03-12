from itertools import permutations
from helpers import test, primes

PRIMES = primes(7)

def check_sub_string_divisibility(n):
    n = str(n)

    for i in range(1, 8):
        sub_string = int(n[i:i+3])

        if sub_string % PRIMES[i - 1] != 0:
            return False

    return True

def find_sub_string_divisibility():
    digits = [str(d) for d in range(10)]
    numbers = []

    for arrangement in permutations(digits):
        if arrangement[0] == 0:
            continue

        n = int(''.join(arrangement))

        if check_sub_string_divisibility(n):
            numbers.append(n)

    return numbers

test(check_sub_string_divisibility(1406357289), True)
test(check_sub_string_divisibility(1046357289), False)
print sum(find_sub_string_divisibility())
