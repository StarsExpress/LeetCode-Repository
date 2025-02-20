
def count_max_increasing_cells(self, matrix: list[list[int]]) -> int:  # LeetCode Q.2713.
    total_rows, total_cols = len(matrix), len(matrix[0])
    if total_rows == 1:  # Base case: only one row.
        return len(set(matrix[0]))  # Answer is simply count of distinct nums.

    self.rows_table = dict()
    for row_idx in range(total_rows):
        self.rows_table.update({row_idx: dict()})

        for col_idx in range(total_cols):
            num = matrix[row_idx][col_idx]
            if num not in self.rows_table[row_idx].keys():
                self.rows_table[row_idx].update(
                    {
                        num: {"indices": [], "prev": None, "cells": 1}
                    }
                )
            self.rows_table[row_idx][num]["indices"].append(col_idx)

        unique_nums = sorted(self.rows_table[row_idx].keys())
        for idx, num in enumerate(unique_nums):
            if idx > 0:
                self.rows_table[row_idx][num]["prev"] = unique_nums[idx - 1]

    self.cols_table = dict()
    for col_idx in range(total_cols):
        self.cols_table.update({col_idx: dict()})

        for row_idx in range(total_rows):
            num = matrix[row_idx][col_idx]
            if num not in self.cols_table[col_idx].keys():
                self.cols_table[col_idx].update(
                    {
                        num: {"indices": [], "prev": None, "cells": 1}
                    }
                )
            self.cols_table[col_idx][num]["indices"].append(row_idx)

        unique_nums = sorted(self.cols_table[col_idx].keys())
        for idx, num in enumerate(unique_nums):
            if idx > 0:
                self.cols_table[col_idx][num]["prev"] = unique_nums[idx - 1]

    self.max_cells = 1  # Base case.
    self.processed_entries = set()  # ID format: str(row idx) + ":" + str(col idx).

    for row_idx in range(total_rows):
        for col_idx in range(total_cols):
            self._dfs_max_cells(matrix[row_idx][col_idx], row_idx, col_idx)

    return self.max_cells

def _dfs_max_cells(self, num: int, row_idx: int, col_idx: int) -> None:
    entry_id = f"{row_idx}:{col_idx}"
    if entry_id not in self.processed_entries:
        best_prev_cells = -float("inf")

        row_prev_num = self.rows_table[row_idx][num]["prev"]
        if row_prev_num is not None:
            for prev_col_idx in self.rows_table[row_idx][row_prev_num]["indices"]:
                self._dfs_max_cells(row_prev_num, row_idx, prev_col_idx)

            row_prev_cells = self.rows_table[row_idx][row_prev_num]["cells"]
            if row_prev_cells > best_prev_cells:
                best_prev_cells = row_prev_cells

        col_prev_num = self.cols_table[col_idx][num]["prev"]
        if col_prev_num is not None:
            for prev_row_idx in self.cols_table[col_idx][col_prev_num]["indices"]:
                self._dfs_max_cells(col_prev_num, prev_row_idx, col_idx)

            col_prev_cells = self.cols_table[col_idx][col_prev_num]["cells"]
            if col_prev_cells > best_prev_cells:
                best_prev_cells = col_prev_cells

        best_prev_cells += 1  # Plus 1: current num > prev row and col nums.
        if best_prev_cells > self.rows_table[row_idx][num]["cells"]:
            self.rows_table[row_idx][num]["cells"] = best_prev_cells

        if best_prev_cells > self.cols_table[col_idx][num]["cells"]:
            self.cols_table[col_idx][num]["cells"] = best_prev_cells

        if best_prev_cells > self.max_cells:
            self.max_cells = best_prev_cells

        self.processed_entries.add(f"{row_idx}:{col_idx}")
