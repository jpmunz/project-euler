#include <iostream>
#include <map>
#include <vector>
#include <math.h>
#include "helpers/divisors.h"

using namespace std;

int main()
{
	int D = 500;

	long long n = ceil(-1 + sqrt(1 + 2*pow(D,2))/2) + 1;
	long long t_n;

	for(;;)
	{
		t_n = (pow(n,2) + n) / 2;
		if(count_divisors(t_n) > D) break;
		n++;
	}

	cout << "Tn: " << t_n << endl;
}
