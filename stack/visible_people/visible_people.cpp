#include <vector>
#include <stack>
using namespace std;

vector<int> count_visibilities(vector<int> &heights) // LeetCode Q.1944.
{
    stack<int> stack; // Heights decreasing monotonic stack.
    vector<int> visible_people;

    reverse(heights.begin(), heights.end());
    for (auto height : heights)
    {
        visible_people.push_back(0);
        while (!stack.empty() && stack.top() < height)
        {
            visible_people.back()++;
            stack.pop();
        }

        if (!stack.empty())
        {
            visible_people.back()++;
            if (stack.top() == height)
            {
                stack.pop();
            }
        }

        stack.push(height);
    }

    reverse(visible_people.begin(), visible_people.end());
    return visible_people;
}
