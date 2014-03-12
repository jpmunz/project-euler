from itertools import combinations
from helpers import test, primes_up_to

def find_prime_family(size, lower_bound, upper_bound):

    families = {}
    primes = sorted(list(primes_up_to(upper_bound)))

    for p in primes:
        if p < lower_bound:
            continue

        digits = str(p)
        num_digits = len(digits)

        for to_replace in range(1, num_digits - 1):
            possible_replacements = combinations(range(num_digits), to_replace)

            for replacements in possible_replacements:
                replacements = list(replacements)
                digit_list = list(digits)

                if all(digit_list[r] == digit_list[replacements[0]] for r in replacements):
                    for r in replacements:
                        digit_list[r] = '*'

                    replaced_digits = ''.join(digit_list)

                    families.setdefault(replaced_digits, [])

                    families[replaced_digits].append(digits)

                    if len(families[replaced_digits]) >= size:
                        return families[replaced_digits]


test(set(find_prime_family(7, 50000, 100000)), set(['56003', '56113', '56333', '56443', '56663', '56773', '56993']))

print find_prime_family(8, 50000, 10000000)
