#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	for(int a = 1; a <= 998; a++)
	{
		for(int b = 1; b < (1000 - a); b++)
		{
			int c = 1000 - a - b;

			if(c == sqrt(pow(a,2) + pow(b,2)))
			{
				cout << "abc: " << a*b*c << endl;
			}
		}
	}
}
