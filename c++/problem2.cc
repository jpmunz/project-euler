#include <iostream>

using namespace std;

int main()
{
    int upper_bound = 4000000;
    
    int f_n_1 = 0;
    int f_n = 1;

    int sum = 0;
    
    while(f_n <= upper_bound)
    {
        if(f_n % 2 == 0)
        {
            sum += f_n;
        }
        
        int swap = f_n + f_n_1;
        f_n_1 = f_n;
        f_n = swap;
    }
    
    cout << "sum: " << (sum - 1) << endl;
}
