from helpers import is_palindrome

print max([x * y for x in range(10**2, 10**3) for y in range(10**2, 10**3) if is_palindrome(x*y)])
