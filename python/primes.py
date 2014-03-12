from math import sqrt

class PrimeSet(set):
    '''
    When asked if a number n is prime queries the DB for a set of RANGE_SIZE numbers centered
    around n, [n - RANGE_SIZE, n + RANGE_SIZE].

    If the range is beyond the highest number recorded, performs a sieve to populate the
    range
    '''

    def __init__(self, range_size=10**7):
        super(PrimeSet, self).__init__()

        self.range_size = range_size
        self.calculate_primes(3, range_size)

    def calculate_primes(self, new_lower_bound, new_upper_bound):
        if new_lower_bound % 2 == 0:
            new_lower_bound -= 1

        new_prime_set = set([])
        composite_set = set([])

        if self:
            for i in range(self.lower_bound, self.upper_bound):
                if i in self:
                    composite_set.add(i)
                else:
                    new_prime_set.add(i)

        for i in range(new_lower_bound, new_upper_bound + 2, 2):
            if not i in composite_set:
                new_prime_set.add(i)

                if i <= sqrt(new_upper_bound):
                    for c in range(i**2, new_upper_bound + 2, 2 * i):
                        composite_set.add(c)

        self.clear()
        for p in new_prime_set:
            self.add(p)

        self.lower_bound = new_lower_bound
        self.upper_bound = new_upper_bound

    def fetch_range(self, n):
        lower_bound = int(max(n - (self.range_size / 2.0), 3))
        upper_bound = int(n + (self.range_size / 2.0))
        self.calculate_primes(lower_bound, upper_bound)

    def __contains__(self, n):
        if n < 2:
            return False
        if n == 2:
            return True

        if (n < self.lower_bound or n > self.upper_bound):
            self.fetch_range(n)

        return super(PrimeSet, self).__contains__(n)

prime_set = PrimeSet(range_size=10**6)


'''
Used to test against http://primes.utm.edu/nthprime/index.php#nth
'''
def get_nth_prime(n):
    count = 0
    i = 2
    while(True):
        if i in prime_set:
            count += 1

            if count == n:
                return i

        i += 1



