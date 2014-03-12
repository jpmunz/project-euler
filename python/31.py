from helpers import test

def count_ways(n, integer_set):
    '''
    Counts the ways n can partitioned into a sum of integers from the given
    set.

    Take one member of the set 'd', for each time 'i' it can be put into 'n', count
    the ways the rest of the set can sum to the remainder (n - d*i). If we put 'd' into
    'n' with no remainder, i.e. (n - d*i) == 0 for some i, then we add 1 to the number
    of ways, since we can make n by doing n = d*i
    '''
    count = 0

    if not integer_set:
        return count

    remaining_set = set([x for x in integer_set])
    d = remaining_set.pop()

    while(True):
        if n <= 0:
            if n == 0:
                count += 1
            break

        count += count_ways(n, remaining_set)
        n -= d

    return count

def p(n):
    return count_ways(n, set(range(1, n+1)))


test(count_ways(4, set([3,1])), 2)
test(count_ways(4, set([2,1])), 3)
test(p(8), 22)
test(count_ways(8, set([1,3,5,7])), 6)

print count_ways(200, set([1, 2, 5, 10, 20, 50, 100, 200]))
