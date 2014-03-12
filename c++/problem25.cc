#include <iostream>
#include "helpers/large.h"

using namespace std;

const int digits = 1000;

int fib(LargeNumber f_n, LargeNumber f_n_1, int term)
{
	if(f_n.digits() >= digits)
		return term;

	return fib(f_n + f_n_1, f_n, term + 1);
}

int main()
{
	cout << fib(LargeNumber(1), LargeNumber(0), 1) << endl;
}
