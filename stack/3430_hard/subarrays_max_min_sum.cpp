#include <deque>
#include <vector>
using namespace std;

long long computeMaxMinSum(vector<int> &nums, int k) //  LeetCode Q.3430.
{
    long long totalMaxMinSum = 0;
    long long windowMaxSum = 0, windowMinSum = 0;

    // Format: {idx, num, shares}. Use long long to prevent overflow.
    deque<tuple<int, int, long long>> maxStack, minStack;

    for (int endIdx = 0; endIdx < nums.size(); endIdx++)
    {
        int startIdx = max(0, endIdx - k + 1);

        // Window start idx slides by 1: must update stacks' info.
        if (startIdx > 0)
        {
            get<2>(maxStack.front())--; // Decrement stack's front num shares.
            windowMaxSum -= get<1>(maxStack.front());

            // Front num out of window.
            if (get<0>(maxStack.front()) < startIdx)
                maxStack.pop_front();

            get<2>(minStack.front())--; // Decrement stack's front num shares.
            windowMinSum -= get<1>(minStack.front());

            // Front num out of window.
            if (get<0>(minStack.front()) < startIdx)
                minStack.pop_front();
        }

        long long num = nums[endIdx];

        while (!maxStack.empty() && get<1>(maxStack.back()) <= num)
        {
            windowMaxSum -= get<1>(maxStack.back()) * get<2>(maxStack.back());
            maxStack.pop_back();
        }

        long long maxShares = min(endIdx + 1, k);
        if (!maxStack.empty())
            maxShares = endIdx - get<0>(maxStack.back());

        maxStack.push_back({endIdx, num, maxShares});
        windowMaxSum += num * maxShares;

        while (!minStack.empty() && get<1>(minStack.back()) >= num)
        {
            windowMinSum -= get<1>(minStack.back()) * get<2>(minStack.back());
            minStack.pop_back();
        }

        long long minShares = min(endIdx + 1, k);
        if (!minStack.empty())
            minShares = endIdx - get<0>(minStack.back());

        minStack.push_back({endIdx, num, minShares});
        windowMinSum += num * minShares;

        totalMaxMinSum += windowMaxSum + windowMinSum;
    }

    return totalMaxMinSum;
}
