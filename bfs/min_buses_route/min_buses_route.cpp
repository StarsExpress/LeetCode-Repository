#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <queue>
using namespace std;

int numBusesToDestination(vector<vector<int>> &routes, int source, int target)
{ // LeetCode Q.815.
    if (source == target)
    { // Base case: source is target.
        return 0;
    }

    unordered_set<int> source_routes;
    unordered_set<int> target_routes;

    // Keys: stations. Values: crossed routes.
    unordered_map<int, unordered_set<int>> stations2routes;
    for (int idx = 0; idx < routes.size(); idx++)
    {
        for (auto station : routes[idx])
        {
            if (station == source)
            {
                source_routes.insert(idx + 1); // Route num = idx + 1.
            }
            if (station == target)
            {
                target_routes.insert(idx + 1); // Route num = idx + 1.
            }

            if (stations2routes.find(station) == stations2routes.end())
            {
                stations2routes[station] = {};
            }
            stations2routes[station].insert(idx + 1); // Route num = idx + 1.
        }
    }

    if (source_routes.empty() || target_routes.empty())
    {
        return -1; // Base case: source or target lacks routes.
    }

    // Keys: route. Values: intersected routes.
    unordered_map<int, unordered_set<int>> routes2routes;
    for (const auto &[station, routes_set] : stations2routes)
    {
        for (int idx_1 = 0; idx_1 < routes_set.size(); idx_1++)
        {
            vector<int> crossed_routes(routes_set.begin(), routes_set.end());

            int route_1 = crossed_routes[idx_1];
            if (routes2routes.find(route_1) == routes2routes.end())
            {
                routes2routes[route_1] = {};
            }

            for (int idx_2 = idx_1; idx_2 < routes_set.size(); idx_2++)
            {
                int route_2 = crossed_routes[idx_2];
                if (routes2routes.find(route_2) == routes2routes.end())
                {
                    routes2routes[route_2] = {};
                }

                routes2routes[route_1].insert(route_2);
                routes2routes[route_2].insert(route_1);
            }
        }
    }

    int min_buses_taken = numeric_limits<int>::max();
    unordered_set<int> visited_routes;

    queue<pair<int, int>> queue; // Format: {route num, count of taken routes}.
    for (auto route : source_routes)
    {
        queue.push({route, 1});
    }

    while (!queue.empty())
    {
        int route = queue.front().first;
        visited_routes.insert(route);
        int buses_taken = queue.front().second;
        queue.pop();

        if (target_routes.find(route) != target_routes.end())
        {
            if (buses_taken < min_buses_taken)
            {
                min_buses_taken = buses_taken;
            }
            continue;
        }

        buses_taken += 1;
        for (auto crossed_route : routes2routes[route])
        {
            if (visited_routes.find(crossed_route) == visited_routes.end())
            {
                queue.push({crossed_route, buses_taken});
            }
        }
    }

    if (min_buses_taken == numeric_limits<int>::max())
    {
        return -1;
    }
    return min_buses_taken;
}
