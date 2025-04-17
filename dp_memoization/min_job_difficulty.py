from collections import deque


class MinJobDifficulty:
    def __init__(self):
        self.total_jobs = 0
        self.difficulties = []
        self.prefix_maxs, self.suffix_maxs, self.prefix_sums = [], deque(), []
        self.table = dict()

    def minimize_schedule_difficulty(self, difficulties: list[int], d: int) -> int:
        self.total_jobs = len(difficulties)
        if self.total_jobs < d:  # Base case.
            return -1

        self.difficulties.clear()
        self.difficulties = difficulties

        self.prefix_maxs.clear()
        self.prefix_sums.clear()
        for difficulty in self.difficulties:
            if not self.prefix_maxs:
                self.prefix_maxs.append(difficulty)

            else:
                self.prefix_maxs.append(max(self.prefix_maxs[-1], difficulty))

            if not self.prefix_sums:
                self.prefix_sums.append(difficulty)

            else:
                self.prefix_sums.append(self.prefix_sums[-1] + difficulty)

        self.suffix_maxs.clear()
        for difficulty in self.difficulties[::-1]:
            if not self.suffix_maxs:
                self.suffix_maxs.appendleft(difficulty)
                continue
            self.suffix_maxs.appendleft(max(self.suffix_maxs[0], difficulty))

        self.table.clear()
        return self._arrange_jobs(0, d)

    def _arrange_jobs(self, start_idx: int, d: int) -> int:
        arrange_id = f"{start_idx}:{d}"
        if arrange_id not in self.table.keys():
            if d == 1:
                max_difficulty = self.suffix_maxs[start_idx]

            else:  # For days >= 2.
                today_difficulty = -float("inf")
                max_difficulty = float("inf")
                for split_idx in range(start_idx, self.total_jobs - 1):
                    if self.total_jobs - 1 - split_idx < d - 1:
                        break  # Not enough remaining jobs for future days.

                    today_difficulty = max(
                        today_difficulty, self.difficulties[split_idx]
                    )
                    if max_difficulty < today_difficulty:
                        break

                    if self.total_jobs - 1 - split_idx == d - 1:
                        future_difficulty = self.prefix_sums[-1]
                        future_difficulty -= self.prefix_sums[split_idx]

                    else:
                        future_difficulty = self._arrange_jobs(split_idx + 1, d - 1)

                    if today_difficulty + future_difficulty < max_difficulty:
                        max_difficulty = today_difficulty + future_difficulty

            self.table.update({arrange_id: max_difficulty})

        return self.table[arrange_id]
