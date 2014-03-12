#include "divisors.h"

long long sum_proper_divisors(long long n)
{
	long long sum = 1;

	if(n == 1)
		return sum;
//
	for(long long i = 2; i <= sqrt(n); i++)
		if(n % i == 0)
			if(i == sqrt(n))
				sum += i;
			else
				sum += (i + n/i);

	return sum;
}

int count_divisors(long long n)
{
	int divisors = 2; //n and 1
	for(long long i = 2; i <= sqrt(n); i++)
	{
		if(n % i == 0)
		{
			if(i == sqrt(n))
				divisors++;
			else
				divisors += 2;
		}
	}

	return divisors;
}

bool is_prime(long long n)
{
	return (count_divisors(n) == 2);
}
