from helpers import test, is_pandigital

def is_concatenation_of_products(n):
    digits = str(n)

    for i in range(1, 9):
        digits_to_try = int(digits[:i])

        p = 2
        while(True):
            product = p * digits_to_try

            product_digits = len(str(product))

            if int(digits[i:i+product_digits]) != product:
                break

            if i+product_digits == len(digits):
                return True

            p += 1
            i += product_digits

    return False


def find_largest_concatenation_of_products():
    lower_bound = 918273645
    upper_bound = 987654321

    for n in range(upper_bound, lower_bound, -1):
        if not is_pandigital(n):
            continue

        if is_concatenation_of_products(n):
            return n

test(is_concatenation_of_products(192384576), True)
test(is_concatenation_of_products(918273645), True)

print find_largest_concatenation_of_products()
