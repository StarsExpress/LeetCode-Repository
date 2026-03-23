#include <vector>
#include <unordered_map>
using namespace std;

int maximumLength(vector<int> &nums, int k) // LeetCode Q.3177.
{
    int max_len = 1; // Base case.

    // ith idx stores best subseq len when using only nums[:i + 1].
    vector<int> prevDiffBest; // Only need latest 2 diffs.
    vector<int> currentDiffBest;

    // At current diff, each num's best subseq len when served as subseq end.
    unordered_map<int, int> nums2Lens;

    for (int diff = 0; diff < k + 1; diff++) // Differences go from 0 to k.
    {
        for (int idx = 0; idx < nums.size(); idx++)
        {
            if (nums2Lens.find(nums[idx]) != nums2Lens.end())
                nums2Lens[nums[idx]] += 1; // Extend subseq w/o changing diff.

            else
                nums2Lens[nums[idx]] = 1; // Base case.

            if (min(diff, idx) > 0) // Can extend previous diff's earlier subseqs.
            {
                if (1 + prevDiffBest[idx - 1] > nums2Lens[nums[idx]])
                    nums2Lens[nums[idx]] = 1 + prevDiffBest[idx - 1];
            }

            if (nums2Lens[nums[idx]] > max_len)
                max_len = nums2Lens[nums[idx]];

            if (idx >= 1 && currentDiffBest[idx - 1] >= nums2Lens[nums[idx]])
                currentDiffBest.push_back(currentDiffBest[idx - 1]);

            else
                currentDiffBest.push_back(nums2Lens[nums[idx]]);
        }

        prevDiffBest.clear(); // Reset for the next diff.

        move(
            currentDiffBest.begin(), currentDiffBest.end(),
            back_inserter(prevDiffBest));

        currentDiffBest.clear();
        nums2Lens.clear();
    }

    return max_len;
}