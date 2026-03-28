#include <vector>
#include <stack>
#include <unordered_map>
using namespace std;

int computeTotalStrengths(vector<int> &strengths)
{ // LeetCode Q.2281.
    long long modulo = pow(10, 9) + 7;

    vector<long long> prefixSums;
    vector<long long> prefixPrefixSums;
    for (int idx = 0; idx < strengths.size(); idx++)
    {
        int strength = strengths[idx];
        if (idx == 0)
        {
            prefixSums.push_back(strength);
            prefixPrefixSums.push_back(strength);
        }
        else
        {
            prefixSums.push_back(prefixSums.back() + strength);
            prefixPrefixSums.push_back(prefixPrefixSums.back() + prefixSums.back());
        }

        prefixSums.back() %= modulo;
        prefixPrefixSums.back() %= modulo;
    }

    long long totalStrengths = 0;
    // Total strengths of subarrays ending at ith idx.
    vector<long long> strengthsSum(strengths.size(), 0);

    stack<vector<int>> stack;    // Format: {idx, strength}.
    int prevMinStrengthIdx = -1; // Idx of the prev min strength.

    // Sum of subarrays ending at current min strength idx.
    long long minStrengthSubarraysSum = 0;

    // Sum of mins of subarrays ending at ith idx.
    unordered_map<int, long long> subarraysMinsSum;

    for (int idx = 0; idx < strengths.size(); idx++)
    {
        int strength = strengths[idx];
        while (!stack.empty() && stack.top()[1] >= strength)
            stack.pop();

        if (stack.empty()) // Current strength < all past strengths.
        {
            // Track strengths after prev min strength and until current strength.
            for (int between_idx = prevMinStrengthIdx + 1; between_idx < idx + 1; between_idx++)
                // In-between strength's weight = its idx + 1.
                minStrengthSubarraysSum += (strengths[between_idx] % modulo) * (between_idx + 1);

            minStrengthSubarraysSum %= modulo;

            strengthsSum[idx] += minStrengthSubarraysSum * strength;
            prevMinStrengthIdx = idx;
        }
        else
        { // Current strength has prev smaller strength.
            int smallerIdx = stack.top()[0];
            long long betweenCount = idx - smallerIdx;

            strengthsSum[idx] += strengthsSum[smallerIdx];

            if (subarraysMinsSum.find(smallerIdx) == subarraysMinsSum.end())
                subarraysMinsSum[smallerIdx] = strengths[smallerIdx] * (smallerIdx + 1);

            long long minsSum = subarraysMinsSum[smallerIdx] % modulo;

            strengthsSum[idx] += (prefixSums[idx] - prefixSums[smallerIdx]) * minsSum;

            subarraysMinsSum[idx] = minsSum + strength * betweenCount;

            long long prefixPrefixSum = betweenCount * prefixSums[idx];
            long long minusTerm = prefixPrefixSums[idx - 1];

            if (smallerIdx >= 1)
                minusTerm -= prefixPrefixSums[smallerIdx - 1];

            strengthsSum[idx] += (prefixPrefixSum - minusTerm) * strength;
        }

        strengthsSum[idx] %= modulo;
        totalStrengths += strengthsSum[idx];
        stack.push({idx, strength});
    }

    return totalStrengths % modulo;
}
