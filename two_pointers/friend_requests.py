
def count_suitable_requests(ages: list[int]):  # LeetCode Q.825.
    ages_count = len(ages)
    if ages_count <= 1:
        return 0

    # Special rule: a person x doesn't send request to person y if either condition is met.
    # 1. age of x < age of y; 2. age of y <= 0.5 * age of x + 7.
    distinct_ages = list(set(ages))
    if len(distinct_ages) == 1:
        if distinct_ages[0] <= 14:  # 2nd condition's threshold.
            return 0
        return ages_count * (ages_count - 1)  # Permutation.

    distinct_ages.sort(reverse=True)  # Sort reversely because of 1st condition.
    distribution = dict(zip(distinct_ages, [0] * len(distinct_ages)))
    for age in ages:
        distribution[age] += 1

    requests_count, senders_count = 0, 0
    for age in distinct_ages:
        if age <= 14:  # 2nd condition's threshold.
            break
        requests_count += distribution[age] * (distribution[age] - 1)  # Permutation.

    senders_idx, receivers_idx = 0, 1
    while True:
        if receivers_idx >= len(distinct_ages):
            if senders_idx >= receivers_idx - 1:
                return requests_count

            senders_idx += 1
            receivers_idx += senders_idx + 1 - receivers_idx
            continue

        senders_count += distribution[distinct_ages[senders_idx]] - senders_count
        if 0.5 * distinct_ages[senders_idx] + 7 < distinct_ages[receivers_idx]:
            requests_count += senders_count * distribution[distinct_ages[receivers_idx]]
            receivers_idx += 1
            continue

        # Go to younger senders as no more receivers meet 1st condition for current senders' age.
        senders_idx += 1
        receivers_idx += senders_idx + 1 - receivers_idx
