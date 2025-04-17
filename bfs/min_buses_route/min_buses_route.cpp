#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <queue>
using namespace std;

int numBusesToDestination(vector<vector<int>> &routes, int source, int target)
{
    if (source == target) // Base case: source is target.
        return 0;

    unordered_set<int> source_routes, target_routes;

    // Keys: stations. Values: crossed routes.
    unordered_map<int, vector<int>> stations2routes;
    for (int idx = 0; idx < routes.size(); idx++)
    {
        for (auto station : routes[idx])
        {
            if (station == source)
                source_routes.insert(idx + 1); // Route num = idx + 1.

            if (station == target)
                target_routes.insert(idx + 1); // Route num = idx + 1.

            if (stations2routes.find(station) == stations2routes.end())
                stations2routes[station] = {};
            stations2routes[station].push_back(idx + 1); // Route num = idx + 1.
        }
    }

    if (source_routes.empty() || target_routes.empty())
        return -1; // Base case: source or target lacks routes.

    unordered_set<int> visited_routes, visited_stations;
    queue<pair<int, int>> queue; // Format: {route num, count of taken routes}.
    for (auto route : source_routes)
        queue.push({route, 1});

    while (!queue.empty())
    {
        auto [route, buses_taken] = queue.front();
        visited_routes.insert(route);
        queue.pop();

        if (target_routes.find(route) != target_routes.end())
            return buses_taken;

        buses_taken += 1;
        for (auto station : routes[route - 1]) // Route num = idx + 1.
        {
            if (visited_stations.find(station) == visited_stations.end())
            {
                visited_stations.insert(station);

                for (auto crossed_route : stations2routes[station])
                {
                    if (visited_routes.find(crossed_route) == visited_routes.end())
                        queue.push({crossed_route, buses_taken});
                }
            }
        }
    }

    return -1;
}
