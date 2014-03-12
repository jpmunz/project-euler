from math import floor, log
from helpers import divisors, primes_up_to

k = 20
p = primes_up_to(k)
a = [floor(log(k) / log(p_i)) for p_i in p]

print int(reduce(lambda x, y: x * y, [p_i**a_i for (p_i, a_i) in zip(p, a)]))
