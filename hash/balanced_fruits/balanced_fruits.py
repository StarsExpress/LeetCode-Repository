
def balance_min_cost_fruits(basket_1: list[int], basket_2: list[int]) -> int:  # LeetCode 2561.
    fruits2diffs, min_fruit = dict(), float("inf")
    for fruit_1, fruit_2 in zip(basket_1, basket_2):
        if min(fruit_1, fruit_2) < min_fruit:
            min_fruit = min(fruit_1, fruit_2)

        if fruit_1 not in fruits2diffs.keys():
            fruits2diffs.update({fruit_1: 0})
        fruits2diffs[fruit_1] += 1

        if fruit_2 not in fruits2diffs.keys():
            fruits2diffs.update({fruit_2: 0})
        fruits2diffs[fruit_2] -= 1

    surplus_fruits, deficit_fruits = [], []
    for fruit, difference in fruits2diffs.items():
        if difference % 2 == 1:
            return -1

        if difference > 0:
            surplus_fruits.append(fruit)
        if difference < 0:
            deficit_fruits.append(fruit)

    surplus_fruits.sort()
    deficit_fruits.sort()
    min_cost = 0
    while surplus_fruits and deficit_fruits:
        if surplus_fruits[0] <= deficit_fruits[0]:
            surplus_idx, deficit_idx = 0, -1  # Pair surplus' min fruit with deficit's max fruit.
            surplus_fruit, deficit_fruit = surplus_fruits[0], deficit_fruits[-1]

        else:
            surplus_idx, deficit_idx = -1, 0  # Pair surplus' max fruit with deficit's min fruit.
            surplus_fruit, deficit_fruit = surplus_fruits[-1], deficit_fruits[0]

        units = min(
            fruits2diffs[surplus_fruit], abs(fruits2diffs[deficit_fruit])
        ) // 2

        if min_fruit * 2 < min(surplus_fruit, deficit_fruit):
            min_cost += min_fruit * 2 * units  # Better to use global min fruit as intermediate.

        else:
            min_cost += min(surplus_fruit, deficit_fruit) * units

        fruits2diffs[surplus_fruit] -= 2 * units
        if fruits2diffs[surplus_fruit] == 0:
            surplus_fruits.pop(surplus_idx)

        fruits2diffs[deficit_fruit] += units * 2
        if fruits2diffs[deficit_fruit] == 0:
            deficit_fruits.pop(deficit_idx)

    return min_cost
