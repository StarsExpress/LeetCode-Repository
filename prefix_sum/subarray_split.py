
class SubarraySplit:  # LeetCode Q.410.
    def __init__(self):
        self.prefix_sum, self.numbers = [], []

    def build_prefix_sum(self, nums: list[int]):
        self.prefix_sum.clear()  # Reset before building prefix sum.
        for idx, number in enumerate(nums):
            if idx == 0:
                self.prefix_sum.append(number)
                continue
            self.prefix_sum.append(self.prefix_sum[-1] + number)

    def check_splittable(self, k, max_sum):
        """
        Greedy algo: check if it's possible to split into k (k >= 1)
        subarrays such that no subarray has a sum greater than max_sum.
        """
        current_sum = 0
        count = 1  # At least one subarray.

        for number in self.numbers:
            if current_sum + number > max_sum:  # Time for next subarray.
                current_sum = number
                count += 1
                if count > k:
                    return False

            else:  # Stay at current subarray.
                current_sum += number

        return True

    def split_array(self, numbers: list[int], k: int):
        """Split into k subarrays such that max subarray sum is minimized."""
        if len(numbers) < k:  # Base case.
            return -1

        self.build_prefix_sum(numbers)
        self.numbers.clear()  # Reset numbers.
        self.numbers.extend(numbers)

        # Binary search rationale: always start 1st subarray at 0th idx.
        smallest_sum = max(numbers)  # Smallest possible max subarray sum.
        largest_sum = self.prefix_sum[-1]  # Largest possible max subarray sum.

        while smallest_sum < largest_sum:
            # Check if it's possible to split with current middle sum as max subarray sum.
            mid_sum = (smallest_sum + largest_sum) // 2

            if self.check_splittable(k, mid_sum):  # Need a smaller max subarray sum.
                largest_sum = mid_sum

            else:  # Need a larger max subarray sum.
                smallest_sum = mid_sum + 1

        return smallest_sum
