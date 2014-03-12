from helpers import fib_up_to

print sum([x for x in fib_up_to(4000000) if x % 2 == 0])
