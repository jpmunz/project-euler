#include <iostream>
#include <sstream>
#include <string>
#include <math.h>

using namespace std;

bool is_palindrome(int product)
{
	stringstream convert;
	convert << product;
	string s = convert.str();

	if(s.length() % 2 != 0)
		return false;

	for(int c = 0; c < s.length(); c++)
	{
		if(s[c] != s[s.length() - 1 - c])
			return false;
	}

	return true;
}

int main()
{
	int digits = 3;
	int highest = 0;

	for(int i = pow(10, digits - 1); i < pow(10, digits); i++)
	{
		for(int j = pow(10, digits - 1); j < pow(10, digits); j++)
		{
			int product = i * j;

			if(is_palindrome(product) && product > highest)
				highest = product;
		}
	}

	cout << "largest palindrome: " << highest << endl;
}
