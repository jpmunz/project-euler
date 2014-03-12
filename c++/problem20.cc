#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<int> number;
	number.push_back(1);
	
	int upper_bound = 100;

	for(int n = 1; n <= upper_bound; n++)
	{
		for(int i = 0; i < number.size(); i++)
		{
			number[i] *= n;
		} 

		for(int i = 0; i < number.size(); i++)
		{
			if(number[i] >= 10)
			{
				int carry_digits = number[i] / 10;
				number[i] %= 10;

				if(i == number.size() - 1)
				{
					number.push_back(carry_digits);
				}
				else
				{
					number[i+1] += carry_digits;
				}
			}
		}
	}
	
	int sum = 0;

	for(int d = 0; d < number.size(); d++)
		sum += number[d];
	
	cout << "sum: " << sum << endl;
}