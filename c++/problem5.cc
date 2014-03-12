#include <iostream>

using namespace std;

bool divisible_up_to(int num, int max_divisor)
{
    for(int i = 2; i <= max_divisor; i++)
    {
        if(num % i != 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int i = 1;
    
    for(;;)
    {
        if(divisible_up_to(i, 20))
            break;        
        
        i++;
    }
    
    cout << "answer: " << i << endl;
}


