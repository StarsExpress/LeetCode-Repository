#include <deque>
#include <vector>
using namespace std;

vector<int> find_window_maximums(vector<int> &nums, int window_size)
{ // LeetCode Q.239.
    vector<int> window_maximums;
    // Nums decreasing monotonic queue. Format: (num, idx).
    deque<pair<int, int>> queue;

    for (int idx = 0; idx < nums.size(); idx++)
    {
        while (!queue.empty() && queue.front().second + window_size <= idx)
        {
            queue.pop_front(); // Max num is no longer in current window.
        }
        while (!queue.empty() && queue.back().first < nums[idx])
        {
            queue.pop_back(); // Bigger nums replace smaller nums.
        }
        queue.push_back({nums[idx], idx});

        if (idx >= window_size - 1)
        { // Can collect rolling window maximums.
            window_maximums.push_back(queue.front().first);
        }
    }

    return window_maximums;
}
