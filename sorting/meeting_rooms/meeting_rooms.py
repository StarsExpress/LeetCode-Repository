import heapq


def find_busiest_room(total_rooms: int, meetings: list[list[int]]) -> int:  # LeetCode Q.2402.
    meetings.sort()
    booked_meetings = [0] * total_rooms  # Idx = room number.
    busiest_room, max_meetings = 0, 0
    awaiting_pool = []  # Format: (inclusive start time, exclusive end time).

    available_rooms = [server_num for server_num in range(total_rooms)]
    deck = []  # Format: (next available time point, room number).

    while meetings or awaiting_pool:
        time_1, time_2 = float("inf"), float("inf")
        if meetings:
            time_1 = meetings[0][0]

        if available_rooms and awaiting_pool:  # Jump to the 1st waiting reservation.
            time_2 = awaiting_pool[0][0]

        if not available_rooms and deck:  # Go to the booked room that frees earliest.
            time_2 = deck[0][0]

        current_time = min(time_1, time_2)  # Update current time.
        while deck and deck[0][0] <= current_time:  # Room(s) may become available.
            _, room_num = heapq.heappop(deck)
            heapq.heappush(available_rooms, room_num)

        if meetings and meetings[0][0] <= current_time:
            awaiting_pool.append(meetings.pop(0))

        while awaiting_pool and available_rooms:
            room_num = heapq.heappop(available_rooms)
            start, end = awaiting_pool.pop(0)
            heapq.heappush(deck, (current_time + end - start, room_num))

            booked_meetings[room_num] += 1
            if booked_meetings[room_num] > max_meetings:
                busiest_room = room_num
                max_meetings = booked_meetings[room_num]

            if booked_meetings[room_num] == max_meetings and room_num < busiest_room:
                busiest_room = room_num

    return busiest_room
