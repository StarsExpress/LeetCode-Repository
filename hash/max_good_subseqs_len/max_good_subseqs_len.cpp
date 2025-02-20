#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int maximumLength(vector<int> &nums, int k) // LeetCode Q.3177.
{
    int max_len = 1; // Base case.

    // ith idx stores best subseq len when using only nums[:i + 1].
    vector<int> prev_diff_best; // Only need latest 2 diffs.
    vector<int> current_diff_best;

    // At current diff, each num's best subseq len when served as subseq end.
    unordered_map<int, int> nums2lens;
    for (int diff = 0; diff < k + 1; diff++) // Differences go from 0 to k.
    {
        for (int idx = 0; idx < nums.size(); idx++)
        {
            if (nums2lens.find(nums[idx]) != nums2lens.end())
            {
                nums2lens[nums[idx]] += 1; // Extend subseq w/o changing diff.
            }
            else
            {
                nums2lens[nums[idx]] = 1; // Base case.
            }

            if (min(diff, idx) > 0) // Can extend previous diff's earlier subseqs.
            {
                if (1 + prev_diff_best[idx - 1] > nums2lens[nums[idx]])
                {
                    nums2lens[nums[idx]] = 1 + prev_diff_best[idx - 1];
                }
            }

            if (nums2lens[nums[idx]] > max_len)
            {
                max_len = nums2lens[nums[idx]];
            }

            if (idx >= 1 && current_diff_best[idx - 1] >= nums2lens[nums[idx]])
            {
                current_diff_best.push_back(current_diff_best[idx - 1]);
            }
            else
            {
                current_diff_best.push_back(nums2lens[nums[idx]]);
            }
        }

        prev_diff_best.clear(); // Reset for the next diff.
        move(
            current_diff_best.begin(), current_diff_best.end(),
            back_inserter(prev_diff_best));
        current_diff_best.clear();
        nums2lens.clear();
    }
    return max_len;
}