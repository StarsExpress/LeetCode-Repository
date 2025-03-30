#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

int mostBooked(int total_rooms, vector<vector<int>> &meetings) // LeetCode Q.2402.
{
    sort( // Sort w.r.t. start time.
        meetings.begin(), meetings.end(),
        [](const vector<int> &a, const vector<int> &b)
        { return a[0] < b[0]; });

    vector<int> meetings_counts(total_rooms, 0); // Each room's meetings held.
    int max_meetings = 0, busiest_room = 0;

    // Min heap. Format: {end time, room num}.
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> occupied_rooms_heap;

    // Min heap. Format: room num.
    priority_queue<int, vector<int>, greater<int>> open_rooms_heap;
    for (int room_num = 0; room_num < total_rooms; room_num++)
    {
        open_rooms_heap.push(room_num);
    }

    queue<long long> queue; // Format: meeting's final end time.
    int meeting_idx = 0;    // Idx of iterated meeting.
    while (meeting_idx < meetings.size())
    {
        while (!occupied_rooms_heap.empty())
        { // Free all rooms whose meetings end before current meeting's start.
            auto [end_time, room_num] = occupied_rooms_heap.top();
            if (end_time > meetings[meeting_idx][0])
            {
                break;
            }
            open_rooms_heap.push(room_num);
            occupied_rooms_heap.pop();
        }

        if (!open_rooms_heap.empty())
        { // Available room: current meeting won't postpone.
            queue.push(meetings[meeting_idx][1]);
            meeting_idx++; // Deal with next meeting.
        }
        else
        { // No available room: current meeting postpones.
            long long min_end_time = occupied_rooms_heap.top().first;
            while (!occupied_rooms_heap.empty())
            { // Free all rooms w/ earliest end time.
                auto [end_time, room_num] = occupied_rooms_heap.top();
                if (end_time > min_end_time)
                {
                    break;
                }
                open_rooms_heap.push(room_num);
                occupied_rooms_heap.pop();
            }

            while (meeting_idx < meetings.size() && queue.size() < open_rooms_heap.size())
            { // Let all available rooms each hold a meeting if possible.
                long long end_time = meetings[meeting_idx][1];
                if (min_end_time > meetings[meeting_idx][0])
                { // Postponed.
                    end_time += min_end_time - meetings[meeting_idx][0];
                }
                queue.push(end_time);
                meeting_idx++;
            }
        }

        while (!queue.empty())
        {
            int room_num = open_rooms_heap.top();
            occupied_rooms_heap.push({queue.front(), room_num});
            queue.pop();
            open_rooms_heap.pop();

            meetings_counts[room_num]++;
            if (meetings_counts[room_num] > max_meetings)
            {
                max_meetings = meetings_counts[room_num], busiest_room = room_num;
            }
            if (meetings_counts[room_num] == max_meetings)
            {
                if (room_num < busiest_room)
                { // Always take the smaller num.
                    busiest_room = room_num;
                }
            }
        }
    }

    return busiest_room;
}
