#include "primes.h"

PrimeHelper::PrimeHelper()
{
	primes[2] = true;
}
	
bool PrimeHelper::is_prime(unsigned int n)
{
	if(n % 2 == 0 && n != 2)
		return false;

	if(primes.find(n) == primes.end())
		primes[n] = (count_divisors(n) == 2);

	return primes[n];
}

vector<unsigned int> PrimeHelper::primes_to(unsigned int n)
{
	vector<unsigned int> result;

	result.push_back(2);

	for(unsigned int i = 3; i <= n; i += 2)
	{
		if(primes.find(i) == primes.end() || primes[i])
		{
			primes[i] = true;
			result.push_back(i);

			if(i <= sqrt(n))
			{
				for(long long c = i*i; c <= n; c += 2*i)
					primes[c] = false;
			}
		}
	}

	return result;
}
