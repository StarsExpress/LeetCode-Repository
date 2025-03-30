#include <vector>
#include <map>
using namespace std;

long long minCost(vector<int> &nums, vector<int> &costs)
{ // LeetCode Q.2448.
    map<int, long long> nums2total_costs;
    for (int idx = 0; idx < nums.size(); idx++)
    {
        nums2total_costs[nums[idx]] += costs[idx];
    }

    vector<int> distinct_nums;
    // Weighted costs: cumulation of each num * its total costs.
    vector<long long> prefix_costs, prefix_weighted_costs;

    for (auto const &pair : nums2total_costs)
    {
        distinct_nums.push_back(pair.first);

        if (prefix_costs.empty())
        {
            prefix_costs.push_back(0);
        }
        else
        {
            prefix_costs.push_back(prefix_costs.back());
        }
        prefix_costs.back() += pair.second;

        if (prefix_weighted_costs.empty())
        {
            prefix_weighted_costs.push_back(0);
        }
        else
        {
            prefix_weighted_costs.push_back(prefix_weighted_costs.back());
        }
        prefix_weighted_costs.back() += pair.first * pair.second;
    }

    long long min_cost = numeric_limits<long long>::max();
    ;
    for (int idx = 0; idx < distinct_nums.size(); idx++)
    {
        long long num = distinct_nums[idx];

        long long cost = prefix_weighted_costs.back() - prefix_weighted_costs[idx];
        cost -= num * (prefix_costs.back() - prefix_costs[idx]);

        if (idx > 0)
        {
            cost += num * (prefix_costs[idx - 1]);
            cost -= prefix_weighted_costs[idx - 1];
        }

        if (cost < min_cost)
        {
            min_cost = cost;
        }
    }

    return min_cost;
}
