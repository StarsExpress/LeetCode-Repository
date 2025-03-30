#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class CoprimeProducts
{ // LeetCode Q.2584.
private:
    unordered_map<int, int> find_primes(int num)
    {
        unordered_map<int, int> primes2counts; // Counts of all occurred primes.
        while (num % 2 == 0)
        {
            primes2counts[2]++;
            num /= 2;
        }

        // Num must be odd now. Increment skips even elements.
        for (int factor = 3; factor * factor <= num; factor += 2)
        {
            while (num % factor == 0)
            {
                primes2counts[factor]++;
                num /= factor;
            }
        }

        if (num > 2)
        { // When num is a prime greater than 2.
            primes2counts[num]++;
        }

        return primes2counts;
    }

public:
    int find_split_idx(vector<int> &nums)
    {
        unordered_map<int, unordered_map<int, int>> nums2primes;
        unordered_map<int, int> prefix_primes, suffix_primes;
        for (auto num : nums)
        {
            if (nums2primes.find(num) == nums2primes.end())
            {
                nums2primes[num] = find_primes(num);
            }

            for (auto &pair : nums2primes[num])
            {
                auto [prime, count] = pair;
                suffix_primes[prime] += count;
            }
        }

        unordered_set<int> common_primes;
        for (int idx = 0; idx < nums.size() - 1; idx++)
        {
            for (auto &pair : nums2primes[nums[idx]])
            {
                auto [prime, count] = pair;
                prefix_primes[prime] += count;
                common_primes.insert(prime);
            }

            for (auto &pair : nums2primes[nums[idx]])
            {
                auto [prime, count] = pair;
                suffix_primes[prime] -= count;
                if (suffix_primes[prime] == 0)
                {
                    if (common_primes.find(prime) != common_primes.end())
                    {
                        common_primes.erase(prime);
                    }
                }
            }

            if (common_primes.empty())
            { // Current idx is the smallest idx to split.
                return idx;
            }
        }
        return -1;
    }
};
