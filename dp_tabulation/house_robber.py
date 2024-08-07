
def rob_max_properties(properties: list[int] | tuple[int]):  # LeetCode Q.198: can't rob back-to-back houses.
    if 1 <= len(properties) <= 2:
        return max(properties)

    two_before_mis, last_mis = properties.pop(0), properties.pop(0)  # MIS: max independent set.
    while properties:
        new_property = properties.pop(0)
        if two_before_mis + new_property > last_mis:  # If two-before set retakes lead.
            last_mis = max(two_before_mis, last_mis)
            two_before_mis += new_property
            two_before_mis, last_mis = last_mis, two_before_mis  # Swap sets for next iteration round.
            continue

        two_before_mis = last_mis  # If two-before set doesn't retake lead, update its value to last set's.

    return max(two_before_mis, last_mis)
