from helpers import test, is_palindrome

def is_dual_palindrome(n):
    return is_palindrome(n) and is_palindrome(bin(n).lstrip('0b'))

def find_dual_palindromes(n):
    return [i for i in range(n) if is_dual_palindrome(i)]

test(is_dual_palindrome(585), True)
test(is_dual_palindrome(9), True)
test(is_dual_palindrome(22), False)
test(is_dual_palindrome(16), False)


print sum(find_dual_palindromes(10**6))
