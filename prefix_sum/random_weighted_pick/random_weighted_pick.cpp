#include <vector>
#include <random>
using namespace std;

class RandomWeightedPick // LeetCode Q.528.
{
private:
    vector<int> cumulatedWeights;
    mt19937 gen;
    uniform_int_distribution<int> distribution;

public:
    RandomWeightedPick(vector<int> &weights)
    {
        for (auto weight : weights)
        {
            if (cumulatedWeights.empty())
                cumulatedWeights.push_back(weight);

            else
                cumulatedWeights.push_back(cumulatedWeights.back() + weight);
        }

        distribution = uniform_int_distribution<int>(1, cumulatedWeights.back());
    }

    int pickIndex()
    {
        int pick = distribution(gen);
        int leftIdx = 0;
        int rightIdx = cumulatedWeights.size() - 1;

        while (leftIdx <= rightIdx)
        {
            int midIdx = (leftIdx + rightIdx) / 2;
            if (cumulatedWeights[midIdx] < pick)
                leftIdx = midIdx + 1;

            else
                rightIdx = midIdx - 1;
        }
        return leftIdx; // Number of cumulated weights < pick.
    }
};
