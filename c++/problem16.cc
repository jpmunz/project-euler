#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<int> number;
	number.push_back(1);
	
	for(int n = 0; n < 1000; n++)
	{
		for(int i = 0; i < number.size(); i++)
		{
			number[i] *= 2;

		} 

		for(int i = 0; i < number.size(); i++)
		{
			if(number[i] >= 10)
			{
				number[i] %= 10;
				if(i == number.size() - 1)
				{
					number.push_back(1);
				}
				else
				{
					number[i+1] ++;
				}
			}
		}
	}
	
	int sum = 0;

	for(int d = 0; d < number.size(); d++)
		sum += number[d];
	
	cout << "sum: " << sum << endl;
}