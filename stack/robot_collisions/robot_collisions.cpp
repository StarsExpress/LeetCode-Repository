#include <vector>
#include <string>
#include <stack>
using namespace std;

vector<int> find_survivors(vector<int> &positions, vector<int> &healths, string directions)
{
    // LeetCode Q.2751.
    vector<vector<int>> robots; // Format: {position, idx}.
    for (int idx = 0; idx < positions.size(); idx++)
    {
        robots.push_back({positions[idx], idx});
    }

    sort( // Sort w.r.t. position.
        robots.begin(), robots.end(),
        [](const vector<int> &a, const vector<int> &b)
        { return a[0] < b[0]; });

    stack<vector<int>> stack; // Format: {health, direction, idx}.
    for (auto robot : robots)
    {
        int idx = robot[1];
        int position = positions[idx], health = healths[idx];

        int direction = 0; // L = 0.
        if (directions[idx] == 'R')
        {
            direction += 1; // R = 1.
        }

        // Collision: prev robot goes right and current robot goes left.
        while (!stack.empty() && stack.top()[1] == 1 && health > 0 && direction == 0)
        {
            if (stack.top()[0] > health)
            { // Prev robot survives.
                stack.top()[0] -= 1;
                health -= health;
            }
            else if (stack.top()[0] == health)
            { // Both robots are removed.
                stack.pop();
                health -= health;
            }
            else
            { // Current robot survives.
                stack.pop();
                health -= 1;
            }
        }

        if (health > 0)
        { // Current robot survives.
            stack.push({health, direction, idx});
        }
    }

    vector<vector<int>> remaining_robots;
    while (!stack.empty())
    { // Only need health and orginal idx.
        remaining_robots.push_back({stack.top()[0], stack.top()[2]});
        stack.pop();
    }

    sort( // Sort w.r.t. original idx.
        remaining_robots.begin(), remaining_robots.end(),
        [](const vector<int> &a, const vector<int> &b)
        { return a[1] < b[1]; });

    vector<int> remaining_healths;
    for (auto robot : remaining_robots)
    {
        remaining_healths.push_back(robot[0]);
    }
    return remaining_healths;
}
