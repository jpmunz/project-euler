#include <iostream>

using namespace std;

int main()
{
	int upper_bound = 1000;
    int sum = 0;
    
	for(int i = 0; i < upper_bound; i++)
	{
        if(i % 3 == 0 || i % 5 == 0)
        {
            sum += i;
        }
	}
    
    cout << "sum: " << sum << endl;
}
