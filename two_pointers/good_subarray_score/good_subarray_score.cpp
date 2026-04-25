#include <vector>
using namespace std;

int findMaxScore(vector<int> &nums, int k) // LeetCode Q.1793.
{
    int subarrayMin = nums[k]; // Base case: subarray of only num at kth idx.
    int maxSubarrayScore = nums[k];

    int leftIdx = k;
    int rightIdx = k;

    int width = 1;

    while (leftIdx >= 0 && rightIdx < nums.size())
    {
        int subarrayScore = subarrayMin * width;
        if (subarrayScore > maxSubarrayScore)
            maxSubarrayScore = subarrayScore;

        if (leftIdx == 0 && rightIdx == nums.size() - 1)
            break;

        if (leftIdx == 0 && rightIdx < nums.size() - 1)
        {
            rightIdx += 1;
            width += 1;
        }

        if (leftIdx > 0 && rightIdx == nums.size() - 1)
        {
            leftIdx -= 1;
            width += 1;
        }

        if (leftIdx > 0 && rightIdx < nums.size() - 1) // Both sides can go.
        {
            if (nums[leftIdx - 1] > nums[rightIdx + 1])
                leftIdx -= 1;

            else
                rightIdx += 1;

            width += 1;
        }

        if (min(nums[leftIdx], nums[rightIdx]) < subarrayMin)
            subarrayMin = min(nums[leftIdx], nums[rightIdx]);
    }

    return maxSubarrayScore;
}
