#include <iostream>
#include <map>
#include <vector>
#include "helpers/primes.h"

using namespace std;

int main()
{
	PrimeHelper p_helper = PrimeHelper();
	vector<unsigned int> primes = p_helper.primes_to(2000000);
	vector<unsigned int>::iterator it;

	long long sum = 0;
	for(it = primes.begin(); it < primes.end(); ++it)
		sum += *it;

	cout << "sum: " << sum << endl;

	for(int i = 2; i <= 10; i++)
	{
		cout << i << " is prime: " << p_helper.is_prime(i) << endl;
	}
}


