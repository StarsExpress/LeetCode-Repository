#include <iostream>
#include <vector>
using namespace std;

vector<int> findAllPrimes(int number)
{
    vector<int> primes;
    if (number <= 1)
        return primes; // Sanity check.

    // From 3 and so on, all primes are odd.
    int currentPrime = 2; // The only even prime is 2.

    while (number > 1)
    {
        if (number % currentPrime == 0)
        {
            primes.push_back(currentPrime);
            number /= currentPrime;
            continue;
        }

        if (currentPrime == 2)
            currentPrime++;

        else
            currentPrime += 2;

        if (currentPrime > sqrt(number) && number > 1)
            currentPrime = number;
    }

    return primes;
}
