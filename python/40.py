from helpers import test

def consecutive_digits(n):
    digits = []

    i = 1

    while(True):
        for d in str(i):
            digits.append(int(d))

        if len(digits) >= n:
            return digits

        i += 1

def evaluate_consecutive_expression():
    digits = consecutive_digits(1000000)

    expression = 1

    for p in range(7):
        expression *= digits[(10**p) - 1]

    return expression


test(consecutive_digits(100)[11], 1)
test(consecutive_digits(100)[18], 4)



print evaluate_consecutive_expression()
