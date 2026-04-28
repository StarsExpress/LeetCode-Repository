#include <vector>
#include <unordered_set>
using namespace std;

int sumFlooredPairs(vector<int> &nums)
{ // LeetCode Q.1862.
    int maxNum = *max_element(nums.begin(), nums.end());
    vector<int> numsCounts(maxNum + 1, 0); // Idx i stores count of num i.

    unordered_set<int> distinctNums;
    for (auto num : nums)
    {
        numsCounts[num] += 1;
        distinctNums.insert(num);
    }

    vector<int> prefixCounts;
    for (int idx = 0; idx < numsCounts.size(); idx++)
    {
        if (idx == 0)
            prefixCounts.push_back(numsCounts[idx]);

        else
            prefixCounts.push_back(prefixCounts.back() + numsCounts[idx]);
    }

    long long flooredPairsSum = 0, modulo = pow(10, 9) + 7;
    for (auto num : distinctNums)
    {
        int maxMultiple = maxNum / num;

        for (int multiple = 1; multiple <= maxMultiple; multiple++)
        {
            long long count = 0, product = num * multiple;

            if (multiple == maxMultiple)
                count += prefixCounts.back();

            else
                count += prefixCounts[product + num - 1];

            count -= prefixCounts[product - 1];

            long long increment = numsCounts[num] % modulo;
            increment *= multiple % modulo;
            increment *= count % modulo;

            flooredPairsSum += increment;
            flooredPairsSum %= modulo;
        }
    }

    return flooredPairsSum;
}
