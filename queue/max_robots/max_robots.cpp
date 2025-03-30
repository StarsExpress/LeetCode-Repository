#include <vector>
#include <queue>
using namespace std;

int count_max_robots(vector<int> &charge_times, vector<int> &running_costs, long long budget)
{
    // LeetCode Q.2398.
    deque<pair<long long, int>> queue; // Format: {charge cost, robot idx}.
    long long running_costs_sum = 0;

    // Left & right indices: start & end indices of consecutive robots.
    int left_idx = 0, max_robots = 0;
    for (int right_idx = 0; right_idx < charge_times.size(); right_idx++)
    {
        while (!queue.empty() && queue.front().second < left_idx)
        {
            queue.pop_front(); // Ensure max cost is within selected range.
        }

        while (!queue.empty() && queue.back().first <= charge_times[right_idx])
        {
            queue.pop_back(); // Prefer bigger charge costs inside queue.
        }
        queue.push_back({charge_times[right_idx], right_idx});

        running_costs_sum += running_costs[right_idx];
        int total_robots = right_idx + 1 - left_idx;
        long long total_cost = queue.front().first + total_robots * running_costs_sum;
        while (total_cost > budget)
        {
            running_costs_sum -= running_costs[left_idx];
            left_idx++;
            total_robots--;
            if (left_idx > right_idx)
            { // Can't select the robot at right idx.
                break;
            }

            while (!queue.empty() && queue.front().second < left_idx)
            {
                queue.pop_front(); // Ensure max cost is within selected range.
            }
            total_cost = queue.front().first + total_robots * running_costs_sum;
        }

        if (total_robots > max_robots)
        {
            max_robots = total_robots;
        }
    }

    return max_robots;
}
