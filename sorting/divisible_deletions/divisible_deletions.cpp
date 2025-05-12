#include <vector>
#include <numeric>
using namespace std;

int count_min_deletions(vector<int> &nums, vector<int> &divided_nums)
{
    // LeetCode Q.2344.
    int min_gcd = divided_nums[0]; // Base case.
    for (int idx = 0; idx < divided_nums.size() - 1; idx++)
    {
        int greatest_common_divisor = gcd(divided_nums[idx], divided_nums[idx + 1]);
        min_gcd = gcd(min_gcd, greatest_common_divisor);
        if (min_gcd == 1)
        { // Coprimes exist.
            break;
        }
    }

    int deletions = 0;
    sort(nums.begin(), nums.end());
    int idx = 0;
    while (idx < nums.size())
    {
        if (min_gcd % nums[idx] == 0)
        {
            return deletions;
        }
        idx++;
        deletions++;
    }

    return -1;
}
