
def rob_max_properties(properties: list[int]) -> int:  # LeetCode Q.213.
    # Constraint: can't rob back-to-back houses. Last and 1st houses are seen as back-to-back.
    if 1 <= len(properties) <= 2:
        return max(properties)

    # 1st iteration on houses 1 to n - 1; 2nd iteration on houses 2 to n.
    backup_properties, max_properties = properties[1:], 0
    properties.pop(-1)
    for i in range(2):
        two_before_mis, last_mis = properties.pop(0), properties.pop(0)  # MIS: max independent set.
        for new_property in properties:
            if two_before_mis + new_property > last_mis:  # If two-before set retakes lead.
                last_mis = max(two_before_mis, last_mis)
                two_before_mis += new_property
                two_before_mis, last_mis = last_mis, two_before_mis  # Swap sets for next iteration round.
                continue

            two_before_mis = last_mis  # If two-before set doesn't retake lead, update its value to last set's.

        if max(two_before_mis, last_mis) > max_properties:
            max_properties = max(two_before_mis, last_mis)

        properties = backup_properties  # Restore for 2nd iteration.

    return max_properties
