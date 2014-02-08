import pyprimes

def validate_pair(p1, p2):
    attempt1 = int(str(p1) + str(p2))
    attempt2 = int(str(p2) + str(p1))

    return (pyprimes.isprime(attempt1) and pyprimes.isprime(attempt2))


def check_has_pair(prime):
    result = []

    digits = str(prime)

    if len(digits) < 2:
        return None

    for d in range(len(digits) - 1):
        p1 = digits[:d+1]
        p2 = digits[d+1:]

        if p1[0] == '0' or p2[0] == '0':
            continue

        if pyprimes.isprime(int(p1)) and pyprimes.isprime(int(p2)) and pyprimes.isprime(int(str(p2) + str(p1))):
            result.append([int(p1), int(p2)])

    return result

existing_sets = []
target = 5

found_match = False
for p in pyprimes.primes():
    prime_pairs = check_has_pair(p)

    if not prime_pairs:
        continue

    for pair in prime_pairs:
        found = [False, False]

        for existing in existing_sets:
            for i, p in enumerate(pair):
                if p in existing:
                    found[i] = True
                else:
                    valid = True
                    for op in existing:
                        if not validate_pair(p, op):
                            valid = False
                            break

                    if valid:
                        existing.add(p)

                        if len(existing) >= target:
                            found_match = True

                        found[i] = True

        if not all(found):
            existing_sets.append(set(pair))

    if found_match:
        break

for existing in existing_sets:
    if len(existing) >= target:
        lowest = []

        for i in range(target):
            l = min(existing)
            existing.remove(l)
            lowest.append(l)

        print "Candidate primes: %s" % lowest
        print "Sum: %s" % sum(lowest)
        print

