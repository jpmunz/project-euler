#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	unsigned int upper_bound = 1001;

	unsigned int sum = 1;
	for(unsigned int n = 3; n <= upper_bound; n += 2)
	{
		double box = 2*(2*(pow(n,2)) - 3*n + 3);
		sum += (unsigned int)box;
	}

	cout << "sum: " << sum << endl;
}
