#include <vector>
#include <deque>
using namespace std;

vector<double> find_sliding_window_median(vector<int> &nums, int k)
{ // LeetCode Q.480.
    vector<double> window_medians;

    deque<int> sorted_nums, median_indices;
    median_indices.push_back(k / 2);
    if (k % 2 == 0)
        median_indices.push_back((k / 2) - 1);

    int left_idx = 0;
    for (int right_idx = 0; right_idx < nums.size(); right_idx++)
    {
        if (right_idx - left_idx == k)
        { // Left num is out of window.
            auto left_num_idx = lower_bound(
                sorted_nums.begin(), sorted_nums.end(), nums[left_idx]);
            sorted_nums.erase(left_num_idx);
            left_idx++;
        }

        auto right_num_idx = lower_bound(
            sorted_nums.begin(), sorted_nums.end(), nums[right_idx]);
        sorted_nums.insert(right_num_idx, nums[right_idx]);

        if (sorted_nums.size() == k)
        { // Eligible to track window median.
            double window_median = 0;
            for (auto median_idx : median_indices)
                window_median += sorted_nums[median_idx];

            if (median_indices.size() == 2)
                window_median /= 2;
            window_medians.push_back(window_median);
        }
    }

    return window_medians;
}
