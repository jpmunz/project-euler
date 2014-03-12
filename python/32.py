from helpers import test, is_pandigital

def is_expression_pandigital(m1, m2, p):
    '''
    The digits 1 to 9 must be included in the expression m1 * m2 = p
    exactly once each
    '''
    return is_pandigital("%s%s%s" % (m1, m2, p))

'''
The only way the expression m1 * m2 = n can have exactly 9 digits is
either when m1 is 4-digits and m2 is 1-digit OR m1 is 3-digits and m2 is 2-digits
'''
def sum_pandigital():
    # Don't double count any products
    products = set([])


    # 4-digit and 1-digit
    for m1 in range(10**3, 10**4):
        for m2 in range(10**0, 10**1):
            p = m1*m2
            if is_expression_pandigital(m1,m2, p):
                products.add(p)
                print "%s * %s = %s" % (m1,m2,p)

    # 3-digit and 2-digit
    for m1 in range(10**2, 10**3):
        for m2 in range(10**1, 10**2):
            p = m1*m2
            if is_expression_pandigital(m1,m2, p):
                products.add(p)
                print "%s * %s = %s" % (m1,m2,p)

    return sum(products)

test(is_expression_pandigital(39, 186, 7254), True)
test(is_expression_pandigital(33, 1216, 7254), False)
test(is_expression_pandigital(39, 186, 725), False)
test(is_expression_pandigital(1209, 7, 8463), False)
print sum_pandigital()
