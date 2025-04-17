#include <vector>
using namespace std;

class RangeModule
{ // LeetCode Q.715.
private:
    vector<pair<int, int>> ranges; // Format: {inclusive left, inclusive right}.

public:
    RangeModule() {}

    void add_range(int left, int right)
    {
        right -= 1; // Change to inclusive right.

        // Idx of the first range w/ start > left.
        int idx = upper_bound(
                      ranges.begin(), ranges.end(), left,
                      [](int val, const pair<int, int> &p)
                      { return val < p.first; }) -
                  ranges.begin();

        if (idx > 0 && ranges[idx - 1].second + 1 >= left)
        {             // Merge prev range.
            idx -= 1; // Insertion idx changes.
            right = max(right, ranges[idx].second);
            ranges[idx].second = right;
        }
        else
        {
            ranges.insert(ranges.begin() + idx, {left, right});
        }

        while (idx + 1 < ranges.size() && ranges[idx + 1].first - 1 <= right)
        {
            right = max(right, ranges[idx + 1].second);
            ranges[idx].second = right;
            ranges.erase(ranges.begin() + idx + 1); // Next range is merged.
        }
    }

    bool query_range(int left, int right)
    {
        right -= 1; // Change to inclusive right.

        int idx = upper_bound(
                      ranges.begin(), ranges.end(), left,
                      [](int val, const pair<int, int> &p)
                      { return val < p.first; }) -
                  ranges.begin();

        if (idx > 0)
        {
            if (ranges[idx - 1].first <= left && right <= ranges[idx - 1].second)
                return true;
        }

        return false;
    }

    void remove_range(int left, int right)
    {
        right -= 1; // Change to inclusive right.

        vector<pair<int, int>> remnant_ranges;

        int idx = upper_bound(
                      ranges.begin(), ranges.end(), left,
                      [](int val, const pair<int, int> &p)
                      { return val < p.first; }) -
                  ranges.begin();

        while (idx < ranges.size() && ranges[idx].first <= right)
        {
            int next_range_right = ranges[idx].second;
            ranges.erase(ranges.begin() + idx); // Next range is removed.

            if (right < next_range_right)
            { // Next range has right side remnant.
                remnant_ranges.push_back({right + 1, next_range_right});
                break; // Won't remove other next ranges.
            }
        }

        while (idx - 1 < ranges.size() && ranges[idx - 1].second >= left)
        {
            auto [prev_range_left, prev_range_right] = ranges[idx - 1];
            ranges.erase(ranges.begin() + idx - 1); // Prev range is removed.

            if (prev_range_left < left) // Prev range has left side remnant.
                remnant_ranges.push_back({prev_range_left, left - 1});

            if (right < prev_range_right) // Prev range has right side remnant.
                remnant_ranges.push_back({right + 1, prev_range_right});

            if (prev_range_left <= left)
            { // Won't remove other prev ranges.
                break;
            }
        }

        for (auto remnant_range : remnant_ranges)
        {
            int idx = upper_bound(
                          ranges.begin(), ranges.end(), remnant_range.first,
                          [](int val, const pair<int, int> &p)
                          { return val < p.first; }) -
                      ranges.begin();

            ranges.insert(ranges.begin() + idx, remnant_range);
        }
    }
};