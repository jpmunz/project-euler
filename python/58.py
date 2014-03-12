from helpers import test, primes_up_to, is_prime

def get_diagonals():
    diagonal_offsets = [2, 4, 6, 8]
    diagonals = [1,1,1,1]

    spiral = 0
    while(True):
        for i, value in enumerate(diagonals):
            diagonals[i] = value + (spiral * 8) + diagonal_offsets[i]

        yield diagonals
        spiral += 1

def find_prime_ratio(required_ratio, upper_bound):
    s = 1
    prime_count = 0

    primes = primes_up_to(upper_bound)

    for diagonals in get_diagonals():

        for d in diagonals:
            if d > upper_bound:
                if is_prime(d, cache_result=False):
                    prime_count += 1
            elif d in primes:
                prime_count += 1

        ratio = (prime_count / float(s * 4))
        if ratio < required_ratio:
            return (2 * s) + 1

        s += 1

diagonals = get_diagonals()


test(diagonals.next(), [3, 5, 7, 9])
test(diagonals.next(), [13, 17, 21, 25])
test(diagonals.next(), [31, 37, 43, 49])
test(diagonals.next(), [57, 65, 73, 81])


print find_prime_ratio(.10, 50000000)

