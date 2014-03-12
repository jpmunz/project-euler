from helpers import test, is_palindrome

def reverse_number(n):
    return int(str(n)[::-1])

def find_lychrel_numbers(upper_bound):
    count = 0

    for n in range(upper_bound):
        if is_lychrel(n):
            print n
            count += 1

    return count

def is_lychrel(n):
    for i in range(1, 50):

        #if n % 10 == 0:
        #    return False

        n += reverse_number(n)

        if is_palindrome(n):
            return False

    return True


test(reverse_number(4321), 1234)
test(is_lychrel(47), False)
test(is_lychrel(349), False)
test(is_lychrel(196), True)
test(is_lychrel(10677), True)

print find_lychrel_numbers(10000)
