from helpers import test, permutate_number, primes_up_to

def find_permutated_prime(lower_bound, upper_bound, required_perms):

    primes = primes_up_to(upper_bound)
    results = []

    for p in primes:
        if p < lower_bound:
            continue

        perms = filter(lambda perm: perm > p and perm in primes, permutate_number(p))

        for i in range(len(perms)):
            for j in range(i + 1, len(perms)):
                if 2 * (perms[i] - p) == perms[j] - p:
                    results.append((p, perms[i], perms[j]))
    return results

perms = permutate_number(418)
test(418 in perms and 481 in perms and 814 in perms, True)

print find_permutated_prime(1000, 10000, 3)
