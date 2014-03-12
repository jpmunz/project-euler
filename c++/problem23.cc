#include <iostream>
#include <vector>
#include <map>
#include "helpers/divisors.h"

using namespace std;

int main()
{
	long long abundant_sum_limit = 20161;

	vector<long long> abundant_numbers;
	map<long long, bool> candidates;
	map<long long, bool>::iterator it;

	for(int i = 12; i <= (abundant_sum_limit-12); i++)
	{
		if(sum_proper_divisors(i) > i)
		{
			abundant_numbers.push_back(i);
			for(int a = 0; a < abundant_numbers.size(); a++)
			{
				long long result = i + abundant_numbers[a];

				if(result <= abundant_sum_limit)
					candidates[result] = true;
			}
		}
	}

	long long sum = 0;
	for(it = candidates.begin(); it != candidates.end(); it++)
		sum += it->first;

	sum = (((long long)pow(abundant_sum_limit,2) + abundant_sum_limit)/2) - sum;
	cout << "sum: " << sum << endl;
}
