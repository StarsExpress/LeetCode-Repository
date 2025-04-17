#include <vector>
using namespace std;

int maximize_frequency_score(vector<int> &nums, long long limit)
{ // LeetCode Q.2968.
    sort(nums.begin(), nums.end());
    vector<long long> prefix_sums;
    for (auto num : nums)
    {
        if (prefix_sums.empty())
        {
            prefix_sums.push_back(num);
            continue;
        }
        prefix_sums.push_back(prefix_sums.back() + num);
    }

    int max_score = 1; // Base case.
    long long operations = 0;

    long long left_idx = 0, mid_idx = 0; // Set long long to prevent overflow.
    for (long long right_idx = 0; right_idx < nums.size(); right_idx++)
    {
        bool first_while = true;
        do
        {
            if (first_while == false)
                left_idx++; // Since 2nd while, the subarray left bound rises.

            // Always optimal to change all nums to the num at mid idx.
            mid_idx = (left_idx + right_idx) / 2;
            operations = prefix_sums[right_idx] - prefix_sums[mid_idx];
            operations -= nums[mid_idx] * (right_idx - mid_idx);

            operations += nums[mid_idx] * (mid_idx - left_idx);
            if (mid_idx > 0)
                operations -= prefix_sums[mid_idx - 1];
            if (left_idx > 0)
                operations += prefix_sums[left_idx - 1];

            first_while = false;
        } while (limit < operations && left_idx < right_idx);

        int score = right_idx + 1 - left_idx;
        if (score > max_score)
            max_score = score;
    }

    return max_score;
}
