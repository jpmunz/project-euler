from copy import copy
from helpers import test, primes_up_to

def find_consecutive_prime_sum(upper_bound):
    primes = primes_up_to(upper_bound)
    sorted_primes = sorted(list(primes))

    longest_sequence = []
    for i in range(len(sorted_primes)):
        sequence = []

        k = 0
        while(True):
            if i + k >= len(sorted_primes):
                break

            sequence.append(sorted_primes[i+k])

            if sum(sequence) > upper_bound:
                break

            if sum(sequence) in primes:
                if len(sequence) > len(longest_sequence):
                    longest_sequence = copy(sequence)

            k += 1
    return longest_sequence


test(sum(find_consecutive_prime_sum(100)), 41)
test(sum(find_consecutive_prime_sum(1000)), 953)

print sum(find_consecutive_prime_sum(1000000))
