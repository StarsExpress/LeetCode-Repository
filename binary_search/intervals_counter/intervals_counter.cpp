#include <vector>
using namespace std;

class IntervalsCounter
{ // LeetCode Q.2276.
private:
    vector<pair<int, int>> ranges; // Format: {inclusive left, inclusive right}.
    int covered_nums = 0;

public:
    IntervalsCounter() {}

    void add(int left, int right)
    {
        int idx = upper_bound(
                      ranges.begin(), ranges.end(), left,
                      [](int val, const pair<int, int> &p)
                      { return val < p.first; }) -
                  ranges.begin();

        if (idx > 0 && ranges[idx - 1].second + 1 >= left)
        {             // Merge prev range.
            idx -= 1; // Insertion idx changes.
            covered_nums -= ranges[idx].second + 1 - ranges[idx].first;
            right = max(right, ranges[idx].second);
            ranges[idx].second = right;
            left = ranges[idx].first;
        }
        else
        {
            ranges.insert(ranges.begin() + idx, {left, right});
        }

        while (idx + 1 < ranges.size() && ranges[idx + 1].first - 1 <= right)
        {
            covered_nums -= ranges[idx + 1].second + 1 - ranges[idx + 1].first;
            right = max(right, ranges[idx + 1].second);
            ranges[idx].second = right;
            ranges.erase(ranges.begin() + idx + 1); // Next range is merged.
        }

        covered_nums += right + 1 - left;
    }

    int count()
    {
        return covered_nums;
    }
};