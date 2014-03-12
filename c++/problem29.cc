#include <iostream>
#include <map>
#include <math.h>

using namespace std;

int main()
{
	int max = 100;

	int doubles = 0;
	map<int, map<int, bool> > base;

	for(int a = 2; pow(a,2) <= max; a++)
	{
		if(base.find(a) != base.end())
			continue;

		map<int, bool> powers_seen;
		int power_factor = 1;

		for(int b = a; b <= max; b *= a)
		{
			for(int power = power_factor*2; power <= (max * power_factor); power += power_factor)
			{
				if(powers_seen.find(power) != powers_seen.end())
					doubles++;
				else
					powers_seen[power] = true;
			}
			
			base[b] = powers_seen;
			power_factor++;
		}
	}

	cout << "Distinct terms: " << pow(max - 1, 2) - doubles << endl; 
}


