#include <vector>
#include <unordered_set>
using namespace std;

int sum_floored_pairs(vector<int> &nums)
{ // LeetCode Q.1862.
    int max_num = *max_element(nums.begin(), nums.end());
    vector<int> nums2counts(max_num + 1, 0); // Idx i stores count of num i.
    unordered_set<int> distinct_nums;
    for (auto num : nums)
    {
        nums2counts[num] += 1;
        distinct_nums.insert(num);
    }

    vector<int> prefix_counts;
    for (int idx = 0; idx < nums2counts.size(); idx++)
    {
        if (idx == 0)
        {
            prefix_counts.push_back(nums2counts[idx]);
        }
        else
        {
            prefix_counts.push_back(prefix_counts.back() + nums2counts[idx]);
        }
    }

    long long floored_pairs_sum = 0, modulo = pow(10, 9) + 7;
    for (auto num : distinct_nums)
    {
        int max_multiple = max_num / num;
        for (int multiple = 1; multiple <= max_multiple; multiple++)
        {
            long long count = 0, product = num * multiple;

            if (multiple == max_multiple)
            {
                count += prefix_counts.back();
            }
            else
            {
                count += prefix_counts[product + num - 1];
            }

            count -= prefix_counts[product - 1];

            long long increment = nums2counts[num] % modulo;
            increment *= multiple % modulo;
            increment *= count % modulo;

            floored_pairs_sum += increment;
            floored_pairs_sum %= modulo;
        }
    }

    return floored_pairs_sum;
}
