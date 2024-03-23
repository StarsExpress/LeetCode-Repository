
class OptimalBST:
    """Optimal binary search tree."""

    def __init__(self, weights_dict: dict[str, int | float]):
        if min(weights_dict.values()) <= 0:
            raise ValueError('All weights must be positive.')

        self.items_list, self.weights_list = list(weights_dict.keys()), list(weights_dict.values())
        self.costs_matrix = [[0] * len(self.weights_list) for _ in range(len(self.weights_list))]
        for i in range(len(self.weights_list)):  # Fill matrix diagonal.
            self.costs_matrix[i][i] += self.weights_list[i]

        # In each subtree, track "candidate" costs and record min cost's root.
        self.candidates_dict, self.roots_dict = dict(), dict()

    def find_subtree_cost(self, row_idx: int, col_idx: int):
        if row_idx > col_idx:
            return 0
        if row_idx == col_idx:
            return self.costs_matrix[row_idx][col_idx]

        if row_idx < col_idx:
            if self.costs_matrix[row_idx][col_idx] != 0:  # No need to recompute if cost isn't 0.
                return self.costs_matrix[row_idx][col_idx]

            self.candidates_dict.clear()  # Clear dict before current iteration's usage.
            for mid_idx in range(row_idx, col_idx + 1):
                candidate = self.find_subtree_cost(row_idx, mid_idx - 1) + self.find_subtree_cost(mid_idx + 1, col_idx)
                self.candidates_dict.update({mid_idx: candidate})

            root_idx = min(self.candidates_dict, key=self.candidates_dict.get)
            self.roots_dict.update({(row_idx, col_idx): root_idx})  # Record lowest cost's root index.
            return min(self.candidates_dict.values()) + sum(self.weights_list[row_idx: col_idx + 1])

    def find_optimal_bst(self, cost_only=False):
        for j in range(len(self.weights_list)):  # Columns iteration from left to right.
            for i in range(len(self.weights_list), -1, -1):  # "Reversed (bottom-up)" rows iteration.
                if i < j:  # Only compute upper triangular parts.
                    self.costs_matrix[i][j] += self.find_subtree_cost(row_idx=i, col_idx=j)

        if cost_only:
            return self.costs_matrix[0][-1]  # Uppermost and rightmost value = optimal cost.


if __name__ == '__main__':
    weights_dictionary = {'1': 0.2, '2': 0.05, '3': 0.17, '4': 0.1, '5': 0.2, '6': 0.03, '7': 0.25}
    optimal_bst = OptimalBST(weights_dictionary)
    print(optimal_bst.find_optimal_bst(True))
