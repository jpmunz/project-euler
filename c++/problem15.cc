#include <iostream>
#include <vector>

using namespace std;


int main()
{
	vector<long long> ways;
	ways.push_back(1);
	ways.push_back(3);
	ways.push_back(6);

	int n = 20;

	for(int i = 3; i <= n; i ++)
	{
		for(int j = 1; j<i; j++)
		{
			ways[j] = ways[j] + ways[j-1];
		}

		ways.push_back(2*ways[i-1]);


		cout << i << ": " << ways[i] << endl;
	}
}
