#include <vector>
#include <stack>
#include <deque>
using namespace std;

vector<int> countVisibilities(vector<int> &heights) // LeetCode Q.1944.
{
    stack<int> stack; // A stack of heights.

    deque<int> visibilities;

    for (int idx = heights.size() - 1; idx >= 0; idx--)
    {
        int height = heights[idx];

        visibilities.push_front(0);

        while (!stack.empty() && stack.top() < height)
        {
            stack.pop();
            visibilities.front()++;
        }

        if (!stack.empty())
        {
            visibilities.front()++;

            if (stack.top() == height)
                stack.pop();
        }

        stack.push(height);
    }

    return vector(visibilities.begin(), visibilities.end());
}
