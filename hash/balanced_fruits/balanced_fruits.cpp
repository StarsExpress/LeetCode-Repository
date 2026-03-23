#include <vector>
#include <map>
#include <queue>
using namespace std;

long long balanceMinCostFruits(vector<int> &basket_1, vector<int> &basket_2)
{ // LeetCode 2561.
    // Each fruit's basket 1 count - basket 2 count.
    map<int, int> fruits2Diffs;
    for (auto fruit : basket_1)
        fruits2Diffs[fruit]++;

    for (auto fruit : basket_2)
        fruits2Diffs[fruit]--;

    // When min balanced fruit exists, its double is min single swap cost.
    long long minBalancedFruit = numeric_limits<int>::max();
    long long minSingleSwapCost = numeric_limits<int>::max();

    vector<deque<int>> surpluses(2); // Basket idx = basket num - 1.

    for (auto &pair : fruits2Diffs)
    {
        auto [fruit, diff] = pair;
        if (diff % 2 == 1)
            return -1;

        if (diff > 0) // Basket 1 has more current fruits.
            surpluses[0].push_back(fruit);

        if (diff < 0) // Basket 2 has more current fruits.
            surpluses[1].push_back(fruit);

        if (diff == 0 && fruit < minBalancedFruit)
            minBalancedFruit = fruit, minSingleSwapCost = fruit * 2;
    }

    long long minTotalCost = 0;
    while (!surpluses[0].empty() && !surpluses[1].empty())
    {
        long long cost_1 = min(surpluses[0].front(), surpluses[1].back());
        long long cost_2 = min(surpluses[0].back(), surpluses[1].front());

        minTotalCost += min(min(cost_1, cost_2), minSingleSwapCost);

        int basket2SurplusSize = surpluses[1].size();
        vector<int> fruitsIndices = {0, basket2SurplusSize - 1};

        if (cost_1 > cost_2)
        {
            int basket1SurplusSize = surpluses[0].size();
            fruitsIndices = {basket1SurplusSize - 1, 0};
        }

        for (int basketNum = 1; basketNum <= 2; basketNum++)
        {
            int basketIdx = basketNum - 1; // Basket num - 1 = basket idx.
            int fruitIdx = fruitsIndices[basketIdx];
            int fruit = surpluses[basketIdx][fruitIdx];

            if (basketNum == 1)
                fruits2Diffs[fruit] -= 2;

            else
                fruits2Diffs[fruit] += 2;

            if (fruits2Diffs[fruit] == 0)
            { // Becomes balanced.
                if (fruit < minBalancedFruit)
                {
                    minBalancedFruit = fruit, minSingleSwapCost = fruit * 2;
                }

                if (fruitIdx == 0)
                    surpluses[basketIdx].pop_front();

                else
                    surpluses[basketIdx].pop_back();
            }
        }
    }

    return minTotalCost;
}
