#include <vector>
#include <map>
#include <queue>
using namespace std;

long long balance_min_cost_fruits(vector<int> &basket_1, vector<int> &basket_2)
{ // LeetCode 2561.
    // Each fruit's basket 1 count - basket 2 count.
    map<int, int> fruits2diffs;
    for (auto fruit : basket_1)
    {
        fruits2diffs[fruit]++;
    }
    for (auto fruit : basket_2)
    {
        fruits2diffs[fruit]--;
    }

    // When min balanced fruit exists, its double is min single swap cost.
    long long min_balanced_fruit = numeric_limits<int>::max();
    long long min_single_swap_cost = numeric_limits<int>::max();

    vector<deque<int>> surpluses(2); // Basket idx = basket num - 1.
    for (auto &pair : fruits2diffs)
    {
        auto [fruit, diff] = pair;
        if (diff % 2 == 1)
        {
            return -1;
        }

        if (diff > 0)
        { // Basket 1 has more current fruits.
            surpluses[0].push_back(fruit);
        }
        if (diff < 0)
        { // Basket 2 has more current fruits.
            surpluses[1].push_back(fruit);
        }

        if (diff == 0 && fruit < min_balanced_fruit)
        {
            min_balanced_fruit = fruit, min_single_swap_cost = fruit * 2;
        }
    }

    long long min_total_cost = 0;
    while (!surpluses[0].empty() && !surpluses[1].empty())
    {
        long long cost_1 = min(surpluses[0].front(), surpluses[1].back());
        long long cost_2 = min(surpluses[0].back(), surpluses[1].front());
        min_total_cost += min(min(cost_1, cost_2), min_single_swap_cost);

        int basket_2_surplus_size = surpluses[1].size();
        vector<int> fruits_indices = {0, basket_2_surplus_size - 1};
        if (cost_1 > cost_2)
        {
            int basket_1_surplus_size = surpluses[0].size();
            fruits_indices = {basket_1_surplus_size - 1, 0};
        }

        for (int basket_num = 1; basket_num <= 2; basket_num++)
        {
            int basket_idx = basket_num - 1; // Basket num - 1 = basket idx.
            int fruit_idx = fruits_indices[basket_idx];
            int fruit = surpluses[basket_idx][fruit_idx];

            if (basket_num == 1)
            {
                fruits2diffs[fruit] -= 2;
            }
            else
            {
                fruits2diffs[fruit] += 2;
            }

            if (fruits2diffs[fruit] == 0)
            { // Becomes balanced.
                if (fruit < min_balanced_fruit)
                {
                    min_balanced_fruit = fruit, min_single_swap_cost = fruit * 2;
                }

                if (fruit_idx == 0)
                {
                    surpluses[basket_idx].pop_front();
                }
                else
                {
                    surpluses[basket_idx].pop_back();
                }
            }
        }
    }

    return min_total_cost;
}
