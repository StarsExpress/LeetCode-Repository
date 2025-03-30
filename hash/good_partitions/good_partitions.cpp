#include <vector>
#include <unordered_map>
using namespace std;

int count_good_partitions(vector<int> &nums)
{ // LeetCode Q.2963.
    // Each num's 1st and last occurred indices.
    unordered_map<int, pair<int, int>> nums2boundary_indices;
    for (int idx = 0; idx < nums.size(); idx++)
    {
        if (nums2boundary_indices.find(nums[idx]) == nums2boundary_indices.end())
        {
            nums2boundary_indices[nums[idx]] = {idx, idx};
        }
        nums2boundary_indices[nums[idx]].second = idx;
    }

    int segments = 0;
    int last_segment_left_idx = -1, last_segment_right_idx = -1;
    for (int idx = 0; idx < nums.size(); idx++)
    {
        auto [left_idx, right_idx] = nums2boundary_indices[nums[idx]];
        if (last_segment_right_idx < left_idx)
        { // A new segment is formed.
            segments += 1;
            last_segment_left_idx = left_idx, last_segment_right_idx = right_idx;
            continue;
        }

        if (last_segment_right_idx < right_idx)
        { // Last segment expands.
            last_segment_right_idx = right_idx;
        }
    }

    long long partitions = 1, modulo = pow(10, 9) + 7;
    while (segments > 1)
    { // Partitions = 2 ** (segments - 1).
        partitions *= 2;
        partitions %= modulo; // Required to control size.
        segments--;
    }
    return partitions;
}
