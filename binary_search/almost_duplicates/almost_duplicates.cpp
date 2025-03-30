#include <vector>
#include <queue>
using namespace std;

bool count_almost_duplicates(vector<int> &nums, int idx_diff, int val_diff)
{
    // LeetCode Q.220.
    queue<int> queue;   // Queue of indices of nums in current window.
    vector<int> window; // Sorted nums within current window.

    for (int idx = 0; idx < nums.size(); idx++)
    {
        if (!queue.empty() && queue.front() < idx - idx_diff)
        {
            int window_idx = upper_bound(window.begin(), window.end(), nums[queue.front()]) - window.begin();
            window.erase(window.begin() + window_idx - 1);
            queue.pop();
        }

        int window_idx = upper_bound(window.begin(), window.end(), nums[idx]) - window.begin();

        if (window_idx < window.size())
        {
            if (abs(window[window_idx] - nums[idx]) <= val_diff)
            {
                return true;
            }
        }

        if (0 < window_idx)
        {
            if (abs(window[window_idx - 1] - nums[idx]) <= val_diff)
            {
                return true;
            }
        }

        window.insert(window.begin() + window_idx, nums[idx]);
        queue.push(idx);
    }

    return false;
}
