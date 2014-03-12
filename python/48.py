from helpers import test

def evaluate_series(n):
    result = 0

    for i in range(1, n+1):
        result += i**i

    return result

test(evaluate_series(10), 10405071317)

print str(evaluate_series(1000))[-10:]
