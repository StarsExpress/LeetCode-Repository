#include <vector>
#include <queue>
using namespace std;

vector<int> query_closest_rooms(vector<vector<int>> &rooms, vector<vector<int>> &queries)
{ // LeetCode Q.1847.
    // Max heap. Format: {min size, preferred ID, idx}.
    priority_queue<vector<int>, vector<vector<int>>, less<vector<int>>> queries_heap;
    for (int idx = 0; idx < queries.size(); idx++)
        queries_heap.push({queries[idx][1], queries[idx][0], idx});

    // Max heap. Format: {room size, room ID}.
    priority_queue<pair<int, int>, vector<pair<int, int>>, less<pair<int, int>>> rooms_heap;
    for (auto room : rooms)
        rooms_heap.push({room[1], room[0]});

    vector<int> ids_pool;

    vector<int> closest_rooms(queries.size(), -1); // Default to no matching rooms.
    while (!queries_heap.empty())
    {
        int min_size = queries_heap.top()[0];
        int preferred_id = queries_heap.top()[1];
        int query_idx = queries_heap.top()[2];
        queries_heap.pop();

        while (!rooms_heap.empty() && rooms_heap.top().first >= min_size)
        {
            int room_id = rooms_heap.top().second;
            rooms_heap.pop();

            auto idx = upper_bound(ids_pool.begin(), ids_pool.end(), room_id);
            ids_pool.insert(idx, room_id);
        }

        if (!ids_pool.empty())
        {
            int idx = upper_bound(
                          ids_pool.begin(), ids_pool.end(), preferred_id) -
                      ids_pool.begin();

            if (idx == 0)
            {
                closest_rooms[query_idx] = ids_pool.front();
                continue;
            }
            if (idx == ids_pool.size())
            {
                closest_rooms[query_idx] = ids_pool.back();
                continue;
            }

            int left_diff = preferred_id - ids_pool[idx - 1];
            int right_diff = ids_pool[idx] - preferred_id;
            if (left_diff <= right_diff)
            { // Tie: choose the min matching ID.
                closest_rooms[query_idx] = ids_pool[idx - 1];
            }
            else
            {
                closest_rooms[query_idx] = ids_pool[idx];
            }
        }
    }

    return closest_rooms;
}
