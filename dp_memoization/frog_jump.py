
def check_crossability(self, stones: list[int]) -> bool:  # LeetCode Q.403.
    total_stones = len(stones)
    self.stones2indices = dict(
        zip(stones, range(total_stones))  # All stones are unique.
    )
    self.stones, self.last_idx = stones, total_stones - 1
    self.jumpability_table = dict()  # Keys: f"{idx}:{jumps made to reach idx}".
    return self._verify_jumpability(0, 0)

def _verify_jumpability(self, idx: int, jump_made: int) -> bool:
    if idx == self.last_idx:
        return True

    hash_id = f"{idx}:{jump_made}"
    if hash_id not in self.jumpability_table.keys():
        self.jumpability_table.update({hash_id: False})
        for next_jump in [jump_made - 1, jump_made, jump_made + 1]:
            if next_jump > 0:
                next_stone = self.stones[idx] + next_jump
                if next_stone in self.stones2indices.keys():
                    next_idx = self.stones2indices[next_stone]
                    self.jumpability_table.update(
                        {hash_id: self._verify_jumpability(next_idx, next_jump)}
                    )
                    if self.jumpability_table[hash_id]:
                        break  # A successful route is found.

    return self.jumpability_table[hash_id]
