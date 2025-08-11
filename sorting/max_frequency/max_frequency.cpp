#include <vector>
using namespace std;

int count_max_frequency(vector<int> &nums, int k, int operations_limit)
{ // LeetCode Q.3346 & 3347.
    sort(nums.begin(), nums.end());

    int max_frequency = 1;           // Base case.
    int prev_num = nums.front() - 1; // Prevent duplicate searches.
    for (auto num : nums)
    {
        if (prev_num < num)
        {
            prev_num = num;
            // Only search for num - k, num and num + k.
            long long candidate_num = num - k;
            while (candidate_num <= num + k)
            {
                int left_mid_idx = lower_bound(
                                       nums.begin(), nums.end(), candidate_num) -
                                   nums.begin();

                int right_mid_idx = upper_bound(
                                        nums.begin(), nums.end(), candidate_num) -
                                    nums.begin() - 1;

                int lower_idx = lower_bound(
                                    nums.begin(), nums.end(), candidate_num - k) -
                                nums.begin();

                int upper_idx = upper_bound(
                                    nums.begin(), nums.end(), candidate_num + k) -
                                nums.begin() - 1;

                int frequency = right_mid_idx + 1 - left_mid_idx;
                int operated_count = left_mid_idx - lower_idx + upper_idx - right_mid_idx;
                frequency += min(operated_count, operations_limit);
                if (frequency > max_frequency)
                    max_frequency = frequency;

                if (k == 0)
                {
                    break;
                }
                candidate_num += k;
            }
        }
    }

    return max_frequency;
}
