#include <vector>
#include <map>
#include <math.h>
#include <iostream>
#include "divisors.h"

using namespace std;

class PrimeHelper
{
public:
	PrimeHelper();
	vector<unsigned int> primes_to(unsigned int n);
	bool is_prime(unsigned int n);
private:
	map<unsigned int, unsigned int> primes;
	map<unsigned int, bool>::iterator it;
};
