#include <vector>
#include <algorithm>
using namespace std;

class MedianFinder
{ // LeetCode Q.295.
private:
    vector<int> nums;

public:
    MedianFinder()
    {
    }

    void addNum(int num)
    {
        int idx = upper_bound(nums.begin(), nums.end(), num) - nums.begin();
        nums.insert(nums.begin() + idx, num);
    }

    double findMedian()
    {
        int midIdx = nums.size() / 2;
        if (nums.size() % 2 == 1)
            return nums[midIdx];

        return (nums[midIdx - 1] + nums[midIdx]) * 0.5;
    }
};