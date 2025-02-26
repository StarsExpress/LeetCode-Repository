#include <vector>
using namespace std;

int minRefuelStops(int target, int startFuel, vector<vector<int>> &stations)
{ // LeetCode Q.871.
    int min_stops = 0;
    int current_position = startFuel;
    startFuel -= startFuel;
    vector<int> fuel_max_heap;

    while (current_position < target)
    {
        // Collect all the visited gas stations.
        while (!stations.empty() && current_position >= stations[0][0])
        {
            fuel_max_heap.push_back(stations[0][1]);
            push_heap(fuel_max_heap.begin(), fuel_max_heap.end());
            stations.erase(stations.begin());
        }

        if (startFuel == 0) // Time to refuel.
        {
            if (fuel_max_heap.empty())
            {
                return -1;
            }

            startFuel += fuel_max_heap[0];
            min_stops += 1;
            pop_heap(fuel_max_heap.begin(), fuel_max_heap.end());
            fuel_max_heap.pop_back();
        }

        current_position += startFuel; // Spend all the fuel to move on.
        startFuel -= startFuel;
    }

    return min_stops;
}
