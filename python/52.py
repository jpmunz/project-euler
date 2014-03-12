from helpers import test

def same_digits(n, m):
    return sorted(str(n)) == sorted(str(m))

def find_same_digit_product(multiplications):
    x = 1

    while(True):
        if all(same_digits(x, x*m) for m in range(2, multiplications+1)):
            return x

        x += 1

test(same_digits(125874, 251748), True)
test(same_digits(425874, 257748), False)
test(find_same_digit_product(2), 125874)


print find_same_digit_product(6)
