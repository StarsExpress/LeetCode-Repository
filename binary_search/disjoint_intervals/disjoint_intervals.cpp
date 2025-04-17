#include <vector>
using namespace std;

class RangesSummary
{ // LeetCode Q.352.
private:
    vector<vector<int>> ranges; // Format: {inclusive left, inclusive right}.

public:
    RangesSummary() {}

    void add_value(int value)
    {
        int left = value, right = value; // Added value itself is a new range.

        int idx = upper_bound(
                      ranges.begin(), ranges.end(), left,
                      [](int val, const vector<int> &v)
                      { return val < v[0]; }) -
                  ranges.begin(); // Idx of the first range w/ start > left.

        if (idx > 0 && ranges[idx - 1][1] + 1 >= left)
        {             // Merge prev range.
            idx -= 1; // Insertion idx changes.
            right = max(right, ranges[idx][1]);
            ranges[idx][1] = right;
        }
        else
        {
            ranges.insert(ranges.begin() + idx, {left, right});
        }

        while (idx + 1 < ranges.size() && ranges[idx + 1][0] - 1 <= right)
        {
            right = max(right, ranges[idx + 1][1]);
            ranges[idx][1] = right;
            ranges.erase(ranges.begin() + idx + 1); // Next range is merged.
        }
    }

    vector<vector<int>> get_intervals()
    {
        return ranges;
    }
};