#include <vector>
#include <queue>
using namespace std;

int countMaxRobots(vector<int> &chargeTimes, vector<int> &runningCosts, long long budget) // LeetCode Q.2398.
{
    int maxRobotsCount = 0; // Base case.

    long long windowTotalCost = 0;

    int startIdx = 0;
    deque<pair<int, int>> queue; // Format: {charge time, idx}.

    for (int endIdx = 0; endIdx < chargeTimes.size(); endIdx++)
    {
        windowTotalCost += runningCosts[endIdx];

        while (!queue.empty() && queue.back().first <= chargeTimes[endIdx])
            queue.pop_back();

        queue.push_back({chargeTimes[endIdx], endIdx});

        int robotsCount = endIdx + 1 - startIdx;
        int maxChargeTime = queue.front().first;

        while (budget < maxChargeTime + robotsCount * windowTotalCost)
        {
            windowTotalCost -= runningCosts[startIdx];

            startIdx++;
            robotsCount--;

            if (!queue.empty() && queue.front().second < startIdx)
                queue.pop_front();

            if (queue.empty())
                break;
        }

        if (robotsCount > maxRobotsCount)
            maxRobotsCount = robotsCount;
    }

    return maxRobotsCount;
}
