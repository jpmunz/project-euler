#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int prime_to_find = 10001;
    int prime_count = 0;
    vector<int> primes;
    
    int i = 2;
    
    for(;;)
    {
        bool divisible = false;
        for(int p = 0; p < primes.size(); p++)
        {
            if(i % primes[p] == 0)
            {
                divisible = true;
                break;
            }
        }
        
        if(!divisible)
        {
            prime_count++;
            
            if(prime_count == prime_to_find)
            {
                cout << "prime: " << i << endl;
                break;
            }
            
            primes.push_back(i);
        }
        
        i++;
    }
}
