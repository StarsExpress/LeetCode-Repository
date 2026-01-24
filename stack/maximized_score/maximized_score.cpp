#include <vector>
#include <stack>
#include <cmath>
#include <algorithm>
using namespace std;

long long modulo = pow(10, 9) + 7;

int count_distinct_primes(int num)
{
    int count = 0;
    if (num <= 1)
        return count; // Sanity check.

    // From 3 and so on, all primes are odd.
    int current_prime = 2; // The only even prime is 2.
    int last_prime = -1;

    while (num > 1)
    {
        if (num % current_prime == 0)
        {
            if (current_prime != last_prime)
                last_prime = current_prime, count++;
            num /= current_prime;
            continue;
        }

        if (current_prime == 2)
            current_prime++;
        else
            current_prime += 2;

        if (current_prime > sqrt(num) && num > 1)
            current_prime = num;
    }

    return count;
}

long long fast_exponentiate(long long base, long long power)
{
    long long product = 1;
    base %= modulo;

    while (power > 0)
    {
        if (power % 2 == 1)
            product = (product * base) % modulo;
        base = (base * base) % modulo;
        power /= 2;
    }

    return product;
}

int maximize_score(vector<int> &nums, long long k) // LeetCode Q.2818.
{
    vector<vector<int>> nums_scores_indices; // Format: {num, prime score, idx}.
    for (int idx = 0; idx < nums.size(); idx++)
    {
        int num = nums[idx];
        nums_scores_indices.push_back({num, count_distinct_primes(num), idx});
    }

    vector<int> prev_non_smaller_indices(nums.size(), -1);
    vector<int> next_bigger_indices(nums.size(), nums.size());

    stack<pair<int, int>> scores_stack; // Format: {prime score, idx}.

    // Next bigger indices search.
    for (int idx = 0; idx < nums_scores_indices.size(); idx++)
    {
        int prime_score = nums_scores_indices[idx][1];

        while (!scores_stack.empty() && scores_stack.top().first < prime_score)
        {
            int prev_idx = scores_stack.top().second;
            next_bigger_indices[prev_idx] = idx;
            scores_stack.pop();
        }

        scores_stack.push({prime_score, idx});
    }

    scores_stack = {}; // Clear for prev non smaller indices search.
    for (int idx = nums_scores_indices.size() - 1; idx >= 0; idx--)
    {
        int prime_score = nums_scores_indices[idx][1];

        while (!scores_stack.empty() && scores_stack.top().first <= prime_score)
        {
            int next_idx = scores_stack.top().second;
            prev_non_smaller_indices[next_idx] = idx;
            scores_stack.pop();
        }

        scores_stack.push({prime_score, idx});
    }

    long long max_score = 1;

    sort(
        nums_scores_indices.begin(), nums_scores_indices.end(),
        [](const vector<int> &a, const vector<int> &b)
        {
            if (a[0] != b[0])
                return a[0] > b[0];
            return a[1] > b[1];
        }); // Sort by descending nums. Break ties by descending prime scores.

    for (auto num_score_idx : nums_scores_indices)
    {
        int num = num_score_idx[0], idx = num_score_idx[2];

        // Must use long long to prevent overflow.
        long long leftmost_idx = prev_non_smaller_indices[idx];
        long long rightmost_idx = next_bigger_indices[idx];
        long long range = (idx - leftmost_idx) * (rightmost_idx - idx);
        long long multiplier = min(range, k);

        max_score *= fast_exponentiate(num, multiplier);
        max_score %= modulo;

        k -= multiplier;
        if (k == 0) // No more operations.
            break;
    }

    return max_score;
}
