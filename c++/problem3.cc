#include <iostream>
#include <math.h>

using namespace std;

bool is_prime(long long n)
{
	if(n % 2 == 0) return false;

	for(long long i = 3; i <= sqrt(n); i+=2)
		if (n % i == 0) return false;

	return true;
}

int main()
{
	long long n = 600851475143;
	long long largest_factor = n;

	for(long long i = 2; i < n; i++)
	{
		if(largest_factor % i == 0)
		{
			largest_factor /= i;

			if(is_prime(largest_factor))
			{
				cout << "largest prime factor: " << largest_factor << endl;
				break;
			}

			i--;
			continue;
		}
	}
}
