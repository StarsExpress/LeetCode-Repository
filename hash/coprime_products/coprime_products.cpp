#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class CoprimeProducts
{ // LeetCode Q.2584.
private:
    unordered_map<int, int> findPrimes(int num)
    {
        unordered_map<int, int> primes2Counts; // Counts of all occurred primes.
        while (num % 2 == 0)
        {
            primes2Counts[2]++;
            num /= 2;
        }

        // Num must be odd now. Increment skips even elements.
        for (int factor = 3; factor * factor <= num; factor += 2)
        {
            while (num % factor == 0)
            {
                primes2Counts[factor]++;
                num /= factor;
            }
        }

        if (num > 2) // When num is a prime greater than 2.
            primes2Counts[num]++;

        return primes2Counts;
    }

public:
    int find_split_idx(vector<int> &nums)
    {
        unordered_map<int, unordered_map<int, int>> nums2Primes;
        unordered_map<int, int> prefixPrimes, suffixPrimes;

        for (auto num : nums)
        {
            if (nums2Primes.find(num) == nums2Primes.end())
                nums2Primes[num] = findPrimes(num);

            for (auto &pair : nums2Primes[num])
            {
                auto [prime, count] = pair;
                suffixPrimes[prime] += count;
            }
        }

        unordered_set<int> commonPrimes;
        for (int idx = 0; idx < nums.size() - 1; idx++)
        {
            for (auto &pair : nums2Primes[nums[idx]])
            {
                auto [prime, count] = pair;
                prefixPrimes[prime] += count;
                commonPrimes.insert(prime);
            }

            for (auto &pair : nums2Primes[nums[idx]])
            {
                auto [prime, count] = pair;
                suffixPrimes[prime] -= count;
                if (suffixPrimes[prime] == 0)
                {
                    if (commonPrimes.find(prime) != commonPrimes.end())
                        commonPrimes.erase(prime);
                }
            }

            if (commonPrimes.empty()) // Current idx is the smallest idx to split.
                return idx;
        }
        return -1;
    }
};
