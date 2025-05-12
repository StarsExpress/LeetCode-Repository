#include <vector>
#include <queue>
using namespace std;

class ReversePairs
{ // LeetCode Q.493.
private:
    int inversions = 0;

    vector<int> merge_arrays(vector<int> nums_1, vector<int> nums_2)
    {
        vector<int> merged_list;
        queue<long long> inversion_nums;
        for (auto num : nums_2)
            inversion_nums.push(num);

        int idx_1 = 0, idx_2 = 0;
        while (idx_1 < nums_1.size() && idx_2 < nums_2.size())
        {
            while (!inversion_nums.empty())
            {
                if (nums_1[idx_1] <= 2 * inversion_nums.front())
                {
                    break;
                }
                inversions += nums_1.size() - idx_1;
                inversion_nums.pop();
            }

            if (nums_1[idx_1] < nums_2[idx_2])
            {
                merged_list.push_back(nums_1[idx_1]);
                idx_1++;
                continue;
            }

            merged_list.push_back(nums_2[idx_2]);
            idx_2++;
        }

        while (idx_1 < nums_1.size())
        {
            while (!inversion_nums.empty())
            {
                if (nums_1[idx_1] <= 2 * inversion_nums.front())
                {
                    break;
                }
                inversions += nums_1.size() - idx_1;
                inversion_nums.pop();
            }

            merged_list.push_back(nums_1[idx_1]);
            idx_1++;
        }

        while (idx_2 < nums_2.size())
        {
            merged_list.push_back(nums_2[idx_2]);
            idx_2++;
        }

        return merged_list;
    }

    vector<int> merge_sort(vector<int> nums)
    {
        if (nums.size() <= 1)
        {
            return nums;
        }

        size_t center_idx = nums.size() / 2;
        vector<int> nums_1(nums.begin(), nums.begin() + center_idx);
        vector<int> nums_2(nums.begin() + center_idx, nums.end());
        return merge_arrays(merge_sort(nums_1), merge_sort(nums_2));
    }

public:
    int count_reverse_pairs(vector<int> &nums)
    {
        merge_sort(nums);
        return inversions;
    }
};