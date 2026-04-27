import heapq


def _compute_multiple(multiplier: int, power: int, modulo: int) -> int:
    # Compute (multiplier ** power) % modulo.
    multiple = 1
    while power > 0:
        if power & 1:
            multiple *= multiplier
            multiple %= modulo

        multiplier *= multiplier
        multiplier %= modulo
        power >>= 1

    return multiple

def compute_final_state(nums: list[int], k: int, multiplier: int) -> list[int]:  # LeetCode Q.3266.
    if multiplier == 1:  # Base case: keep multiplying 1.
        return nums

    min_heap: list[tuple[int, int]] = []  # Format: (num, idx).
    max_num = nums[0]
    for idx, num in enumerate(nums):
        heapq.heappush(min_heap, (num, idx))
        if num > max_num:
            max_num = num

    while k > 0:
        k -= 1
        _, idx = heapq.heappop(min_heap)
        nums[idx] *= multiplier
        heapq.heappush(min_heap, (nums[idx], idx))
        if nums[idx] > max_num:  # Cycle begins.
            min_heap.clear()  # Reset.
            break

    modulo = 10 ** 9 + 7
    power = k // len(nums)  # Common power for every num.
    common_multiple = _compute_multiple(multiplier, power, modulo)

    for idx, num in enumerate(nums):
        nums[idx] *= common_multiple
        heapq.heappush(min_heap, (nums[idx], idx))
        nums[idx] %= modulo

    k %= len(nums)
    while k > 0:
        k -= 1
        _, idx = heapq.heappop(min_heap)
        nums[idx] *= multiplier  # Extra multiplier.
        nums[idx] %= modulo

    return nums
