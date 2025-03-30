#include <vector>
using namespace std;

int erase_overlapping_intervals(vector<vector<int>> &intervals)
{ // LeetCode Q.435.
    // For a given interval start, always choose the smallest end.
    int initial_size = intervals.size();
    sort(intervals.begin(), intervals.end());

    vector<vector<int>> final_intervals = {intervals.front()};
    intervals.erase(intervals.begin()); // Base case.

    for (auto interval : intervals)
    {
        // Extend: last interval end <= current interval start.
        if (final_intervals.back()[1] <= interval[0])
        {
            final_intervals.push_back(interval);
        }
        // Replace: current interval end < last interval end.
        if (interval[1] < final_intervals.back()[1])
        {
            final_intervals.back() = interval;
        }
    }

    return initial_size - final_intervals.size();
}
