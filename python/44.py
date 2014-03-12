from helpers import test, pentagonal_number

def find_pentagonal_sum_and_difference():
    pentagonals = set([])

    n = 1
    while(True):
        pn = pentagonal_number(n)

        for previous in pentagonals:
            diff = pn - previous

            if diff != previous \
                and diff in pentagonals \
                and abs(diff - previous) in pentagonals:

                return ((previous, diff), abs(diff-previous))

        pentagonals.add(pn)
        n += 1

test(pentagonal_number(1), 1)
test(pentagonal_number(4), 22)
test(pentagonal_number(7), 70)
test(pentagonal_number(8), 92)

print find_pentagonal_sum_and_difference()
