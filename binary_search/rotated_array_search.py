
class RotatedArraySearch:  # LeetCode Q.33 & 81.
    def __init__(self) -> None:
        self.nums = []

    def _search_rotated_idx(self, start_idx: int, end_idx: int) -> int | None:
        if end_idx - start_idx == 2:  # Base case: 3 numbers.
            if self.nums[start_idx] <= self.nums[start_idx + 1] <= self.nums[end_idx]:
                return None
            if self.nums[start_idx] > self.nums[start_idx + 1]:  # 312 format.
                return start_idx + 1
            return end_idx  # 231 format.

        mid_idx = (start_idx + end_idx) // 2
        rotated_idx = self._search_rotated_idx(start_idx, mid_idx + 1)
        if rotated_idx is not None:
            return rotated_idx

        return self._search_rotated_idx(mid_idx, end_idx)

    def search(self, nums: list[int], target: int) -> bool:
        total_nums = len(nums)
        if total_nums <= 2:
            return True if target in nums else False

        self.nums.clear()  # Reset before search.
        self.nums.extend(nums)
        rotated_idx = self._search_rotated_idx(0, total_nums - 1)
        if rotated_idx is not None:
            left_indices = [0, rotated_idx]
            right_indices = [rotated_idx - 1, total_nums - 1]

        else:
            left_indices, right_indices = [0], [total_nums - 1]

        for left_idx, right_idx in zip(left_indices, right_indices):
            while left_idx <= right_idx:
                mid_idx = (left_idx + right_idx) // 2
                if nums[mid_idx] == target:
                    return True

                if nums[mid_idx] < target:
                    left_idx = mid_idx + 1
                    continue
                right_idx = mid_idx - 1

        return False
