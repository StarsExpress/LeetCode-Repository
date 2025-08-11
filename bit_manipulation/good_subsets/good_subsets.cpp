#include <vector>
#include <unordered_map>
using namespace std;

class GoodSubsets
{ // LeetCode Q.1994.
private:
    pair<bool, vector<int>> find_primes(int num)
    {
        vector<int> primes;

        bool repeated_prime = false;
        while (num % 2 == 0)
        {
            if (repeated_prime)
                return {false, primes};

            primes.push_back(2);
            num /= 2;
            repeated_prime = true;
        }

        int prime = 3;
        repeated_prime = false;

        while (num / prime > 0)
        {
            if (num % prime == 0)
            {
                if (repeated_prime)
                    return {false, primes};

                primes.push_back(prime);
                num /= prime;
                repeated_prime = true;
            }
            else
            {
                prime += 2;
                repeated_prime = false;
            }
        }

        return {true, primes};
    }

public:
    int count_good_subsets(vector<int> &nums)
    {
        int max_num = *max_element(nums.begin(), nums.end());

        unordered_map<int, pair<bool, vector<int>>> nums2properties;
        unordered_map<int, int> primes2indices;
        int prime_idx = 0; // Assign each occurred prime a bit idx.

        for (int num = 2; num <= max_num; num++)
        {
            auto [good_num, primes] = find_primes(num);
            nums2properties[num] = {good_num, primes};
            if (good_num && primes.size() == 1)
            { // Num is a prime.
                primes2indices[num] = prime_idx;
                prime_idx++;
            }
        }

        unordered_map<int, int> nums2counts;
        vector<int> distinct_not_1_nums;
        for (auto num : nums)
        {
            nums2counts[num]++;
            if (num > 1 && nums2counts[num] == 1)
                distinct_not_1_nums.push_back(num);
        }

        unordered_map<int, vector<vector<int>>> good_subsets, new_good_subsets;

        for (auto num : distinct_not_1_nums)
        {
            auto [good_num, primes] = nums2properties[num];
            if (good_num)
            {
                for (auto &pair : good_subsets)
                {
                    int past_subset_id = pair.first;
                    int joined_subset_id = pair.first;
                    bool joinable = true; // If num can join past subset.

                    for (auto prime : primes)
                    {
                        int prime_idx = primes2indices[prime];
                        if ((past_subset_id >> prime_idx) & 1)
                        {
                            joinable = false;
                            break;
                        }
                        joined_subset_id |= (1 << prime_idx); // Set bit.
                    }

                    if (joinable)
                        new_good_subsets[joined_subset_id] = good_subsets[past_subset_id];
                }

                for (auto &pair : new_good_subsets)
                {
                    for (auto subset : pair.second)
                    {
                        subset.push_back(num);
                        good_subsets[pair.first].push_back(subset);
                    }
                }
                new_good_subsets.clear(); // Clear for future usage.

                int new_subset_id = 0;
                for (auto prime : primes)
                {
                    int prime_idx = primes2indices[prime];
                    new_subset_id |= (1 << prime_idx); // Set bit.
                }
                good_subsets[new_subset_id].push_back({num});
            }
        }

        // Each subset's base count = (2 ** count of 1) % modulo.
        long long base_count = 1, base = 2, exponent = nums2counts[1];
        long long modulo = pow(10, 9) + 7;
        while (exponent > 0)
        {
            if (exponent & 1)
                base_count = (base_count * base) % modulo;
            base = (base * base) % modulo;
            exponent >>= 1;
        }

        long long total_good_subsets = 0;
        for (auto &pair : good_subsets)
        {
            for (auto subset : pair.second)
            {
                long long count = base_count;
                for (auto num : subset)
                {
                    count *= nums2counts[num];
                    count %= modulo;
                }

                total_good_subsets += count;
                total_good_subsets %= modulo;
            }
        }

        return total_good_subsets;
    }
};