#include <iostream>
#include <math.h>
#include <map>
#include <string>

using namespace std;

int num_letters(int i)
{
	map<int, string> ones;
	map<int, string> teens;
	map<int, string> tens;

	ones[1] = "one";
	ones[2] = "two";
	ones[3] = "three";
	ones[4] = "four";
	ones[5] = "five";
	ones[6] = "six";
	ones[7] = "seven";
	ones[8] = "eight";
	ones[9] = "nine";

	teens[0] = "ten";
	teens[1] = "eleven";
	teens[2] = "twelve";
	teens[3] = "thirteen";
	teens[4] = "fourteen";
	teens[5] = "fifteen";
	teens[6] = "sixteen";
	teens[7] = "seventeen";
	teens[8] = "eighteen";
	teens[9] = "nineteen";

	tens[2] = "twenty";
	tens[3] = "thirty";
	tens[4] = "forty";
	tens[5] = "fifty";
	tens[6] = "sixty";
	tens[7] = "seventy";
	tens[8] = "eighty";
	tens[9] = "ninety";

	int place = 0;
	int sum = 0;

	int units_value = i % 10;
	int tens_value = i % 100;
	
	bool needs_and = (units_value != 0) || (tens_value != 0);

	//teens are a special case
	if(tens_value >= 10 && tens_value <= 19)
	{
		sum += teens[units_value].length();
		i /= 100;
		place = 2;
	}
		
	while(i > 0)
	{
		int place_value = i % 10;

		if(place_value != 0)
		{
			switch(place)
			{
				case 0:
					sum += ones[place_value].length();
					break;
				case 1:
					sum += tens[place_value].length();
					break;
				case 2:
					sum += ones[place_value].length() + string("hundred").length(); //hundred
					break;
				case 3:
					sum += ones[place_value].length() + string("thousand").length();
					break;
			}
		}
	
		i /= 10;
		place++;
	}

	if(needs_and && place >= 3)
		sum += string("and").length();

	return sum;
}

int main()
{
	int sum = 0;

	for(int i = 1; i <= 1000; i++)
	{
		sum += num_letters(i);
	}

	cout << "sum: " << sum << endl;
}

