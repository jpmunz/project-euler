#include <iostream>
#include <map>
#include <vector>
#include <math.h>
#include "helpers/divisors.h"

using namespace std;

int main()
{
	int upper_bound = 10000;

	long long sum = 0;

	for(int i = 1; i < upper_bound; i++)
	{
		int divisor_sum = sum_proper_divisors(i);

		if(divisor_sum > i)
		{
			int partner_sum = sum_proper_divisors(divisor_sum);

			if(partner_sum == i)
				sum += (i + divisor_sum);
		}
	}

	cout << "sum: " << sum << endl;
}
