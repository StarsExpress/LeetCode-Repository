#include <vector>
#include <stack>
using namespace std;

int find_largest_rectangle(vector<int> &heights) // LeetCode Q.84.
{
    vector<int> prevSmallerIndices(heights.size(), -1);

    int maxArea = 0;

    stack<pair<int, int>> nextStack, prevStack; // Format: {idx, height}.

    for (int idx = 0; idx < heights.size(); idx++)
    {
        int height = heights[idx];

        // Prev smaller search.
        while (!prevStack.empty() && prevStack.top().second >= height)
            prevStack.pop();

        if (!prevStack.empty())
            prevSmallerIndices[idx] = prevStack.top().first;

        prevStack.push({idx, height});

        // Next smaller search.
        while (!nextStack.empty() && nextStack.top().second > height)
        {
            int prevIdx = nextStack.top().first;
            nextStack.pop();

            int width = idx - prevSmallerIndices[prevIdx] - 1;
            int area = heights[prevIdx] * width;
            if (area > maxArea)
                maxArea = area;
        }

        nextStack.push({idx, height});
    }

    while (!nextStack.empty())
    {
        int idx = nextStack.top().first;
        nextStack.pop();

        int width = heights.size() - prevSmallerIndices[idx] - 1;
        int area = heights[idx] * width;
        if (area > maxArea)
            maxArea = area;
    }

    return maxArea;
}
