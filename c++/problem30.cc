#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	int n = 5;

	//Determine max number needed to check
	int digits = 1;
	double max_sum;
	for(;;)
	{
		max_sum = pow(9, n) * digits;

		if(max_sum < pow(10, digits + 1))
			break;

		digits++;
	}

	double total = 0;

	for(int i = 2; i <= max_sum; i++)
	{
		double sum = 0;
		int num = i;

		while(num > 0)
		{
			sum += pow((num % 10), n);
			num /= 10;
		}

		if(sum == i)
			total += sum;
	}

	cout << "total: " << total << endl;

}
