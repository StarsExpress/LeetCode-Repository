
def calculate_min_cost(nums: list[int], costs: list[int]) -> int:  # LeetCode Q.2448.
    nums2total_costs: dict[int, int] = dict()
    for idx, num in enumerate(nums):
        if num not in nums2total_costs.keys():
            nums2total_costs.update({num: 0})
        nums2total_costs[num] += costs[idx]

    nums2total_costs = dict(sorted(nums2total_costs.items()))
    distinct_nums = list(nums2total_costs.keys())

    prefix_costs, prefix_total_costs = [], []
    for num, total_costs in nums2total_costs.items():
        if not prefix_costs:
            prefix_costs.append(0)

        else:
            prefix_costs.append(prefix_costs[-1])

        prefix_costs[-1] += total_costs

        if not prefix_total_costs:
            prefix_total_costs.append(0)

        else:
            prefix_total_costs.append(prefix_total_costs[-1])

        prefix_total_costs[-1] += num * total_costs

    min_cost = float("inf")
    for idx, num in enumerate(distinct_nums):
        total_cost = prefix_total_costs[-1] - prefix_total_costs[idx]
        total_cost -= num * (prefix_costs[-1] - prefix_costs[idx])

        if idx > 0:
            total_cost += num * prefix_costs[idx - 1]
            total_cost -= prefix_total_costs[idx - 1]

        if total_cost < min_cost:
            min_cost = total_cost

    return min_cost
