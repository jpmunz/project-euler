import pyprimes

start = 1

increments = [2, 4, 6, 8]
diagonal = [start] * 4

primes = 0
composites = 1
spirals = 0

target_ratio = .10

while True:
    spirals += 1
    for i in range(len(diagonal)):
        diagonal[i] += increments[i]
        increments[i] += 8

        if pyprimes.isprime(diagonal[i]):
            primes += 1
        else:
            composites += 1

    if (primes / (primes + float(composites))) < target_ratio:
        break

side_length = (2 * (spirals + 1)) - 1

print "Side length: %s" % side_length
