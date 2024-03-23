
class Knapsack:
    """Knapsack calculator."""

    def __init__(self, values_dict: dict[str, int | float], weights_dict: dict[str, int], capacity: int):
        if values_dict.keys() != weights_dict.keys():
            raise ValueError('Values and weights dicts should have same keys and orders.')
        if capacity <= 0:
            raise ValueError('Capacity should be positive.')

        self.items_list, self.capacity = list(values_dict.keys()), capacity
        self.values_list, self.weights_list = list(values_dict.values()), list(weights_dict.values())
        self.values_matrix = [[0] * (1 + capacity) for _ in range(len(self.values_list))]  # 1 is for capacity = 0 case.

    def find_best_combination(self, value_only=False):
        extra_value = 0  # Extra value: item value + value at (i - 1, j - item weight) - value at (i - 1, j).

        for i in range(len(self.values_list)):  # Rows (items) iteration.
            for j in range(1, self.capacity + 1):  # Columns (capacities) iteration.
                # Value at (i, j) >= value at (i - 1, j) as value at (i - 1, j) is an "inheritance".
                self.values_matrix[i][j] += self.values_matrix[i - 1][j]
                if self.weights_list[i] > j:  # If item weight > capacity.
                    continue

                extra_value += self.values_list[i] + self.values_matrix[i - 1][j - self.weights_list[i]]
                extra_value -= self.values_matrix[i - 1][j]
                self.values_matrix[i][j] += max(extra_value, 0)
                extra_value -= extra_value  # Return to zero for next iteration's usage.

        if value_only:
            return max(max(self.values_matrix))


if __name__ == '__main__':
    from config import DATA_FOLDER_PATH
    import os

    values_dictionary, weights_dictionary = dict(), dict()
    items = open(os.path.join(DATA_FOLDER_PATH, 'knapsack', 'knapsack_100.txt'), 'r').readlines()
    total_capacity = int(items[0].split(' ')[0])  # 1st line tells capacity.
    for item in items[1:]:
        value, weight = item.split(' ')
        values_dictionary.update({str(len(values_dictionary) + 1): int(value)})
        weights_dictionary.update({str(len(weights_dictionary) + 1): int(weight)})

    knapsack = Knapsack(values_dictionary, weights_dictionary, total_capacity)
    print(f'Optimal knapsack value: {knapsack.find_best_combination(True)}')
