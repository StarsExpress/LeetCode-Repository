
def verify_square(point_1: list[int], point_2: list[int], point_3: list[int], point_4: list[int]):  # LeetCode Q.593.
    if point_1 == point_2 == point_3 == point_4:  # In case 4 points are identical.
        return False
    mid_x = (point_1[0] + point_2[0] + point_3[0] + point_4[0]) / 4  # Mid point's x value.
    mid_y = (point_1[1] + point_2[1] + point_3[1] + point_4[1]) / 4  # Mid point's y value.

    # Quadrilaterals have 4 "half slants" in it. Only need these from middle point to point 1, 2 & 4.
    half_slant_1 = (mid_x - point_1[0]) ** 2 + (mid_y - point_1[1]) ** 2
    half_slant_2 = (mid_x - point_2[0]) ** 2 + (mid_y - point_2[1]) ** 2
    half_slant_4 = (mid_x - point_4[0]) ** 2 + (mid_y - point_4[1]) ** 2

    # Condition 1: half slants 1 & 2 & 4 all equal.
    if half_slant_1 == half_slant_2 == half_slant_4:
        # Condition 2: sum of half slants 1 & 2 = dist of point 1 & 2 or point 1 & 3.
        if half_slant_1 + half_slant_2 in [(point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2,
                                           (point_1[0] - point_3[0]) ** 2 + (point_1[1] - point_3[1]) ** 2]:
            return True
    return False
