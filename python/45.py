from helpers import test, hexagonal_number, is_pentagonal_number, is_hexagonal_number

def find_pentagonal_and_hexagonal(lower_bound):
    n = lower_bound + 1

    while(True):
        hn = hexagonal_number(n)

        if is_pentagonal_number(hn):
            return hn

        n += 1

test(hexagonal_number(1), 1)
test(hexagonal_number(2), 6)
test(hexagonal_number(3), 15)

test(is_pentagonal_number(22), True)
test(is_pentagonal_number(24), False)
test(is_hexagonal_number(45), True)
test(is_hexagonal_number(46), False)

test(find_pentagonal_and_hexagonal(1), 40755)
print find_pentagonal_and_hexagonal(143)
