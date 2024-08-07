
class Knapsack:
    def __init__(
        self,
        values_dict: dict[str, int | float],
        weights_dict: dict[str, int],
        capacity: int,
    ):
        if values_dict.keys() != weights_dict.keys():
            raise ValueError("Values and weights dicts should have same keys and orders.")
        if capacity <= 0:
            raise ValueError("Capacity should be positive.")

        self.capacity = capacity
        self.item_values, self.weights = list(values_dict.values()), list(weights_dict.values())

        # 1 is for capacity = 0 case.
        self.best_values = [[0] * (1 + capacity) for _ in range(len(self.item_values))]

    def find_best_combination(self, value_only=False):
        extra_value = 0  # Extra value: item value + value at (i - 1, j - item weight) - value at (i - 1, j).

        for i in range(len(self.item_values)):  # Rows (items) iteration.
            for j in range(1, self.capacity + 1):  # Columns (capacities) iteration.
                # Value at (i, j) >= value at (i - 1, j) as value at (i - 1, j) is an "inheritance".
                self.best_values[i][j] += self.best_values[i - 1][j]
                if self.weights[i] > j:  # If item weight > capacity.
                    continue

                extra_value += self.item_values[i] + self.best_values[i - 1][j - self.weights[i]]
                extra_value -= self.best_values[i - 1][j]

                self.best_values[i][j] += max(extra_value, 0)
                extra_value -= extra_value  # Reset to zero for next iteration.

        if value_only:
            return max(max(self.best_values))


if __name__ == "__main__":
    import os
    from config import DATA_FOLDER_PATH

    values_dictionary, weights_dictionary = dict(), dict()
    items = open(os.path.join(DATA_FOLDER_PATH, "knapsack", "knapsack_100.txt"), "r").readlines()
    total_capacity = int(items[0].split(" ")[0])  # 1st line tells capacity.
    for item in items[1:]:
        value, weight = item.split(" ")
        values_dictionary.update({str(len(values_dictionary) + 1): int(value)})
        weights_dictionary.update({str(len(weights_dictionary) + 1): int(weight)})

    knapsack = Knapsack(values_dictionary, weights_dictionary, total_capacity)
    print(f"Optimal knapsack value: {knapsack.find_best_combination(True)}")
