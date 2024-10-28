import heapq


class SeatsManager:  # LeetCode Q.1845.
    def __init__(self, n: int) -> None:
        self.unreserved_seats = [number for number in range(1, n + 1)]

    def reserve(self) -> int:
        return heapq.heappop(self.unreserved_seats)

    def cancel(self, seat_number: int) -> None:
        heapq.heappush(self.unreserved_seats, seat_number)
