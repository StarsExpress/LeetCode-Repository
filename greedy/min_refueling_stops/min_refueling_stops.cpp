#include <vector>
#include <algorithm>
using namespace std;

int minRefuelStops(int target, int startFuel, vector<vector<int>> &stations)
{ // LeetCode Q.871.
    int minStops = 0;
    int currentPosition = startFuel;

    startFuel -= startFuel;
    vector<int> fuelMaxHeap;

    while (currentPosition < target)
    {
        // Collect all the visited gas stations.
        while (!stations.empty() && currentPosition >= stations[0][0])
        {
            fuelMaxHeap.push_back(stations[0][1]);
            push_heap(fuelMaxHeap.begin(), fuelMaxHeap.end());
            stations.erase(stations.begin());
        }

        if (startFuel == 0) // Time to refuel.
        {
            if (fuelMaxHeap.empty())
                return -1;

            startFuel += fuelMaxHeap[0];
            minStops += 1;
            pop_heap(fuelMaxHeap.begin(), fuelMaxHeap.end());
            fuelMaxHeap.pop_back();
        }

        currentPosition += startFuel; // Spend all the fuel to move on.
        startFuel -= startFuel;
    }

    return minStops;
}
