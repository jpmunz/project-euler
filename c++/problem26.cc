#include <iostream>
#include <map>
#include <math.h>

using namespace std;

int main()
{
	int upper_bound = 1000;

	int best_d = 0;
	int max_cycle = 0;
	for(int i = 2; i <= upper_bound; i++)
	{
		map<int, bool> used_divisors;
		int divisor = 1;
		int cycle = 1;

		for(;;)
		{
			while(divisor < i)
				divisor *= 10;

			if(divisor % i == 0)
				break;

			if(used_divisors.find(divisor) == used_divisors.end())
				used_divisors[divisor] = true;
			else
				break;

			divisor -= i;
			cycle++;
		}
		
		if(cycle > max_cycle)
		{
			max_cycle = cycle;
			best_d = i;
		}
	}

	cout << "d with longest cycle: " << best_d << endl;
}
