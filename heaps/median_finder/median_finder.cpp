#include <vector>
using namespace std;

class MedianFinder
{ // LeetCode Q.295.
private:
    vector<int> nums;

public:
    MedianFinder()
    {
    }

    void add_num(int num)
    {
        int idx = upper_bound(nums.begin(), nums.end(), num) - nums.begin();
        nums.insert(nums.begin() + idx, num);
    }

    double find_median()
    {
        int mid_idx = nums.size() / 2;
        if (nums.size() % 2 == 1)
        {
            return nums[mid_idx];
        }
        return (nums[mid_idx - 1] + nums[mid_idx]) * 0.5;
    }
};