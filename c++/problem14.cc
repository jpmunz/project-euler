#include <iostream>
#include <map>
#include <vector>
#include <math.h>

using namespace std;

long long chain_length(long long n)
{
	if(n == 1)
		return 1;
	else if(n % 2 == 0)
		return 1 + chain_length(n/2);
	else
		return 1 + chain_length(3*n + 1);

}
int main()
{
	long long upper_bound = 1000000;
	long long max_length = 0;
	long long candidate = 0;

	for(long long i = 1; i < upper_bound; i++)
	{
		long long cur_length = chain_length(i);

		if(max_length < cur_length)
		{
			max_length = cur_length;
			candidate = i;
		}
	}

	cout << "winner: " << candidate << endl;
}


