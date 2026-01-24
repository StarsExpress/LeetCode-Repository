#include <iostream>
#include <vector>
using namespace std;

vector<int> find_all_primes(int number)
{
    vector<int> primes;
    if (number <= 1)
        return primes; // Sanity check.

    // From 3 and so on, all primes are odd.
    int current_prime = 2; // The only even prime is 2.

    while (number > 1)
    {
        if (number % current_prime == 0)
        {
            primes.push_back(current_prime);
            number /= current_prime;
            continue;
        }

        if (current_prime == 2)
            current_prime++;
        else
            current_prime += 2;

        if (current_prime > sqrt(number) && number > 1)
            current_prime = number;
    }

    return primes;
}
