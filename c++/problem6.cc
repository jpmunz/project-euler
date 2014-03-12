#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int upper_bound = 100;
    
    int sum = 0;
    int sum_of_squares = 0;
    
    for(int i = 1; i <= upper_bound; i++)
    {
        sum += i;
        sum_of_squares += pow(i, 2);
    }
        
    cout << fixed << "difference: " << (pow(sum,2) - sum_of_squares) << endl;
}
