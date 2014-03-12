from helpers import test

def sum_digits(n):
    return sum([int(d) for d in str(n)])


def find_max_sum(upper_bound):
    largest_sum = 0

    for a in range(upper_bound + 1):
        for b in range(upper_bound + 1):
            largest_sum = max(largest_sum, sum_digits(a**b))

    return largest_sum

test(sum_digits(432), 9)

print find_max_sum(100)
