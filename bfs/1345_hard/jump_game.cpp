#include <vector>
#include <list>
#include <unordered_map>
#include <unordered_set>
#include <queue>
using namespace std;

int count_min_jumps(vector<int> &nums)
{ // LeetCode Q.1345.
    int last_idx = nums.size() - 1;

    // Keys: occurred nums. Values: corresponding indices.
    unordered_map<int, list<int>> nums2indices;
    for (int idx = 0; idx < nums.size(); idx++)
    {
        if (nums2indices.find(nums[idx]) == nums2indices.end())
        {
            nums2indices[nums[idx]] = {};
        }
        nums2indices[nums[idx]].push_front(idx);
    }

    int jumps = 0;
    queue<pair<int, int>> queue = {}; // Format: {idx, jumps}.
    queue.push({0, jumps});
    unordered_set<int> visited_indices;

    while (!queue.empty())
    {
        int idx = queue.front().first;
        jumps = queue.front().second;
        if (idx == last_idx)
        {
            break;
        }
        visited_indices.insert(idx);
        queue.pop();

        for (auto neighbor_idx : {idx - 1, idx + 1})
        {
            if (visited_indices.find(neighbor_idx) == visited_indices.end())
            {
                if (0 <= neighbor_idx && neighbor_idx <= last_idx)
                {
                    queue.push({neighbor_idx, jumps + 1});
                }
            }
        }

        for (auto same_value_idx : nums2indices[nums[idx]])
        { // Same value indices.
            if (visited_indices.find(same_value_idx) == visited_indices.end())
            {
                queue.push({same_value_idx, jumps + 1});
            }
        }
        nums2indices[nums[idx]].clear(); // Critical: avoid reprocessing.
    }

    return jumps;
}
