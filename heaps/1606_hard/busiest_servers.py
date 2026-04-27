import heapq


def _binary_search(target: int, sorted_integers: list[int], size: int) -> int:
    if size == 0:
        return 0

    back_idx, front_idx = 0, size - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_integers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of ints < target, implying insertion idx.


def find_busiest_servers(k: int, arrival: list[int], load: list[int]) -> list[int]:  # LeetCode Q.1606.
    requests = [0] * k  # Idx = server's number.
    busiest_servers, max_requests = [], 0

    available_servers = [server_num for server_num in range(k)]
    availability = k  # Number of available servers.
    deck = []  # Format: (next available time point, server number).

    for idx, (arrival_time, load_amount) in enumerate(zip(arrival, load)):
        while deck and deck[0][0] <= arrival_time:  # Server(s) may become available.
            _, server_num = heapq.heappop(deck)
            insertion_idx = _binary_search(server_num, available_servers, availability)
            available_servers.insert(insertion_idx, server_num)
            availability += 1

        if availability == 0:  # Request must be dropped.
            continue

        smaller_count = _binary_search(idx % k, available_servers, availability)
        if smaller_count == availability:  # All servers with numbers < idx % k.
            smaller_count = 0  # Have to take the smallest-numbered server.
        server_num = available_servers.pop(smaller_count)
        availability -= 1

        heapq.heappush(deck, (arrival_time + load_amount, server_num))
        requests[server_num] += 1
        if requests[server_num] > max_requests:
            busiest_servers.clear()
            max_requests = requests[server_num]

        if requests[server_num] == max_requests:
            busiest_servers.append(server_num)

    return busiest_servers
