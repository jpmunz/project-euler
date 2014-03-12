#include <iostream>
#include <map>
#include "math.h"
#include "helpers/primes.h"

using namespace std;

int main()
{
	int max_consecutive = 0;
	int product = 0;

	int min_term = -999;
	int max_term = 1000;

	PrimeHelper p_helper = PrimeHelper();

	vector<unsigned int> primes = p_helper.primes_to(2*max_term + 1);

	map<unsigned int, vector<int> > b_set;
	map<unsigned int, vector<int> >::iterator b_it;

	for(unsigned int p = 0; p < primes.size() && primes[p] < max_term; p++)
	{
		vector<int> b = vector<int>();

		int start = -primes[p] + 2;

		if(start < min_term)
			start = min_term;

		for(int a = start; a < max_term; a++)
		{
			unsigned int next = a + primes[p] + 1;
			if(is_prime(next))
				b.push_back(a);
		}

		b_set[primes[p]] = b;
	}

	unsigned int n = 2;

	for(;;)
	{
		double n_2 = pow(n,2);

		vector<unsigned int> invalid_b;

		for(b_it = b_set.begin(); b_it != b_set.end(); ++b_it)
		{
			unsigned int b = b_it->first;
			vector<int> remaining_a;

			int sum = (int)n_2 + b;
			for(int i = 0; i < b_it->second.size(); i++)
			{
				int a = b_it->second[i];

				if(p_helper.is_prime((n*a) + sum))
					remaining_a.push_back(a);

			}

			if(remaining_a.empty())
				invalid_b.push_back(b);

			b_it->second = remaining_a;

		}

		for(int i = 0; i < invalid_b.size(); i++)
			b_set.erase(invalid_b[i]);

		if(b_set.size() == 1 && b_set.begin()->second.size() == 1)
		{
			int a = b_set.begin()->second[0];
			int b = b_set.begin()->first;
			cout << "a: " << a << ", b: " << b << ", product: " << (a*b) << endl;
			break;
		}

		n++;
	}

}		
