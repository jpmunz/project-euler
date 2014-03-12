import math

def _calculate_step(n, m_prev, denominator, cycle, seen, verbose=False):
    m = math.floor((math.sqrt(n) + m_prev) / float(denominator))
    cycle.append(m)

    m = m_prev - (m * denominator)

    numerator = denominator
    denominator = n - (m**2)

    if not denominator:
        if verbose:
            print "Rational root"
        return []

    m = m * -1
    denominator = denominator / numerator

    if verbose:
        print "cycle: %s" % cycle
        print
        print "root(%s) + %s" % (n, m)
        print "-------------"
        print "     %s      " % denominator


    if (denominator, m) in seen:
        return cycle
    else:
        seen.add((denominator, m))
        return _calculate_step(n, m, denominator, cycle, seen)

def continued_fraction(n, verbose=False):
    return _calculate_step(n, 0, 1, [], set(), verbose=verbose)

upper = 10000
odd_periods = 0
for i in range(2, upper + 1):
    cycle = continued_fraction(i)

    if cycle:
        period = len(cycle) - 1
        if period % 2 != 0:
            odd_periods += 1

print "Odd periods: %s" % odd_periods
