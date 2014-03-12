from helpers import test, prime_factors

def distinct_factors(n):
    return len(prime_factors(n, distinct=True))

def consecutive_numbers_n_distinct_factors(n):
    i = 2

    while(True):
        for k in range(n):
            if distinct_factors(i + k) != n:
                break
        else:
            return [i + k for k in range(n)]

        i += k + 1


test(distinct_factors(14), 2)
test(distinct_factors(644), 3)

test(consecutive_numbers_n_distinct_factors(2), [14, 15])
test(consecutive_numbers_n_distinct_factors(3), [644, 645, 646])

print consecutive_numbers_n_distinct_factors(4)
