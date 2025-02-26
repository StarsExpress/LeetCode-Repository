#include <vector>
#include <random>
using namespace std;

class RandomWeightedPick // LeetCode Q.528.
{
private:
    vector<int> cumulated_weights;
    mt19937 gen;
    uniform_int_distribution<int> distribution;

public:
    RandomWeightedPick(vector<int> &weights)
    {
        for (auto weight : weights)
        {
            if (cumulated_weights.empty())
            {
                cumulated_weights.push_back(weight);
            }
            else
            {
                cumulated_weights.push_back(cumulated_weights.back() + weight);
            }
        }

        distribution = uniform_int_distribution<int>(1, cumulated_weights.back());
    }

    int pickIndex()
    {
        int pick = distribution(gen);
        int left_idx = 0;
        int right_idx = cumulated_weights.size() - 1;
        while (left_idx <= right_idx)
        {
            int mid_idx = (left_idx + right_idx) / 2;
            if (cumulated_weights[mid_idx] < pick)
            {
                left_idx = mid_idx + 1;
            }
            else
            {
                right_idx = mid_idx - 1;
            }
        }
        return left_idx; // Number of cumulated weights < pick.
    }
};
