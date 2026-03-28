#include <vector>
#include <map>
using namespace std;

long long minCost(vector<int> &nums, vector<int> &costs)
{ // LeetCode Q.2448.
    map<int, long long> numsTotalCosts;

    for (int idx = 0; idx < nums.size(); idx++)
        numsTotalCosts[nums[idx]] += costs[idx];

    vector<int> distinctNums;
    // Weighted costs: cumulation of each num * its total costs.
    vector<long long> prefixCosts, prefixWeightedCosts;

    for (auto const &pair : numsTotalCosts)
    {
        distinctNums.push_back(pair.first);

        if (prefixCosts.empty())
            prefixCosts.push_back(0);

        else
            prefixCosts.push_back(prefixCosts.back());

        prefixCosts.back() += pair.second;

        if (prefixWeightedCosts.empty())
            prefixWeightedCosts.push_back(0);

        else
            prefixWeightedCosts.push_back(prefixWeightedCosts.back());

        prefixWeightedCosts.back() += pair.first * pair.second;
    }

    long long minCost = numeric_limits<long long>::max();

    for (int idx = 0; idx < distinctNums.size(); idx++)
    {
        long long num = distinctNums[idx];

        long long cost = prefixWeightedCosts.back() - prefixWeightedCosts[idx];
        cost -= num * (prefixCosts.back() - prefixCosts[idx]);

        if (idx > 0)
        {
            cost += num * (prefixCosts[idx - 1]);
            cost -= prefixWeightedCosts[idx - 1];
        }

        if (cost < minCost)
            minCost = cost;
    }

    return minCost;
}
