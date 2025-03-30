#include <vector>
#include <stack>
#include <unordered_map>
using namespace std;

int compute_total_strengths(vector<int> &strengths)
{ // LeetCode Q.2281.
    long long modulo = pow(10, 9) + 7;

    vector<long long> prefix_sums;
    vector<long long> prefix_prefix_sums;
    for (int idx = 0; idx < strengths.size(); idx++)
    {
        int strength = strengths[idx];
        if (idx == 0)
        {
            prefix_sums.push_back(strength);
            prefix_prefix_sums.push_back(strength);
        }
        else
        {
            prefix_sums.push_back(prefix_sums.back() + strength);
            prefix_prefix_sums.push_back(
                prefix_prefix_sums.back() + prefix_sums.back());
        }

        prefix_sums.back() %= modulo;
        prefix_prefix_sums.back() %= modulo;
    }

    long long total_strengths = 0;
    // Total strengths of subarrays ending at ith idx.
    vector<long long> strengths_sum(strengths.size(), 0);

    stack<vector<int>> stack;       // Format: {idx, strength}.
    int prev_min_strength_idx = -1; // Idx of the prev min strength.
    // Sum of subarrays ending at current min strength idx.
    long long min_strength_subarrays_sum = 0;

    // Sum of mins of subarrays ending at ith idx.
    unordered_map<int, long long> subarrays_mins_sum;

    for (int idx = 0; idx < strengths.size(); idx++)
    {
        int strength = strengths[idx];
        while (!stack.empty() && stack.top()[1] >= strength)
        {
            stack.pop();
        }

        if (stack.empty())
        { // Current strength < all past strengths.
            // Track strengths after prev min strength and until current strength.
            for (int between_idx = prev_min_strength_idx + 1; between_idx < idx + 1; between_idx++)
            {
                // In-between strength's weight = its idx + 1.
                min_strength_subarrays_sum += (strengths[between_idx] % modulo) * (between_idx + 1);
            }
            min_strength_subarrays_sum %= modulo;

            strengths_sum[idx] += min_strength_subarrays_sum * strength;
            prev_min_strength_idx = idx;
        }
        else
        { // Current strength has prev smaller strength.
            int smaller_idx = stack.top()[0];
            long long between_count = idx - smaller_idx;

            strengths_sum[idx] += strengths_sum[smaller_idx];

            if (subarrays_mins_sum.find(smaller_idx) == subarrays_mins_sum.end())
            {
                subarrays_mins_sum[smaller_idx] = strengths[smaller_idx] * (smaller_idx + 1);
            }

            long long mins_sum = subarrays_mins_sum[smaller_idx] % modulo;

            strengths_sum[idx] += (prefix_sums[idx] - prefix_sums[smaller_idx]) * mins_sum;

            subarrays_mins_sum[idx] = mins_sum + strength * between_count;

            long long prefix_prefix_sum = between_count * prefix_sums[idx];
            long long subtract_term = prefix_prefix_sums[idx - 1];
            if (smaller_idx >= 1)
            {
                subtract_term -= prefix_prefix_sums[smaller_idx - 1];
            }

            strengths_sum[idx] += (prefix_prefix_sum - subtract_term) * strength;
        }

        strengths_sum[idx] %= modulo;
        total_strengths += strengths_sum[idx];
        stack.push({idx, strength});
    }

    return total_strengths % modulo;
}
