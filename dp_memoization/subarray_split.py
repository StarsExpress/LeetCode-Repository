
class SplitSubarraySum:  # LeetCode Q.410.
    def __init__(self):
        self.nums, self.prefix_sums = [], []
        self.table = dict()

    def find_min_subarray_sum(self, nums: list[int], k: int) -> int:
        self.nums.clear()
        self.nums.extend(nums)

        self.prefix_sums.clear()
        for num in self.nums:
            if not self.prefix_sums:
                self.prefix_sums.append(num)
                continue
            self.prefix_sums.append(self.prefix_sums[-1] + num)

        self.table.clear()
        return self._split_arrays(0, k)

    def _split_arrays(self, start_idx: int, k: int) -> int:
        array_id = f"{start_idx}:{k}"
        if array_id not in self.table.keys():
            total_sum = self.prefix_sums[-1]
            if start_idx > 0:
                total_sum -= self.prefix_sums[start_idx - 1]

            if k == 1:
                self.table.update({array_id: total_sum})

            else:  # For k >= 2.
                largest_subarray_sum = self.prefix_sums[-1]
                for split_idx in range(start_idx, len(self.nums)):
                    if len(self.nums) - 1 - split_idx < k - 1:
                        break

                    prefix_sum = self.prefix_sums[split_idx]
                    if start_idx > 0:
                        prefix_sum -= self.prefix_sums[start_idx - 1]

                    if largest_subarray_sum < prefix_sum:
                        break

                    if len(self.nums) - 1 - split_idx == k - 1:
                        max_sum = max(self.nums[split_idx + 1:])

                    else:
                        max_sum = self._split_arrays(split_idx + 1, k - 1)

                    if max(max_sum, prefix_sum) < largest_subarray_sum:
                        largest_subarray_sum = max(max_sum, prefix_sum)

                self.table.update({array_id: largest_subarray_sum})

        return self.table[array_id]
