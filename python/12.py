from helpers import divisors


required_divisors = 500

n = 1
while True:
    tn = (n * (n + 1)) / 2
    if len(divisors(tn)) > required_divisors:
        print tn
        break

    n += 1

    if tn >= 76576500:
        print "hi"
        break
