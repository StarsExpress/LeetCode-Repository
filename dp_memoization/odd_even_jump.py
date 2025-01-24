
def _binary_search(target: int, sorted_integers: list[int], size: int) -> int:
    back_idx, front_idx = 0, size - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_integers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of ints < target, implying insertion idx.

def count_good_starting_indices(numbers: list[int]) -> int:  # LeetCode Q.975.
    """
    When can ith idx jump to the rightmost idx? If ith number has a non-smaller number
    to its right, and this non-smaller number can make an even jump to the rightmost number.
    """
    total_numbers = len(numbers)
    next_non_smaller_indices: list[int | None] = [None] * total_numbers
    next_non_greater_indices: list[int | None] = [None] * total_numbers

    nums2indices = dict()
    distinct_nums, total_distinct_nums = [], 0

    total_good_starting_indices = 1  # Base case: rightmost idx is always good.
    # Standing at idx i, can it make an odd jump to the rightmost idx?
    odd_jump_availability = {total_numbers - 1: True}
    # Standing at idx i, can it make an even jump to the rightmost idx?
    even_jump_availability = {total_numbers - 1: True}

    for idx in range(total_numbers - 1, -1, -1):  # Backward iteration.
        number = numbers[idx]
        if number in nums2indices.keys():
            next_non_smaller_indices[idx] = nums2indices[number]
            next_non_greater_indices[idx] = nums2indices[number]

        else:
            insertion_idx = _binary_search(number, distinct_nums, total_distinct_nums)
            if insertion_idx > 0:
                smaller_num = distinct_nums[insertion_idx - 1]
                next_non_greater_indices[idx] = nums2indices[smaller_num]

            if insertion_idx < total_distinct_nums:
                greater_num = distinct_nums[insertion_idx]
                next_non_smaller_indices[idx] = nums2indices[greater_num]

            distinct_nums.insert(insertion_idx, number)
            total_distinct_nums += 1

        nums2indices.update({number: idx})  # Update number's min idx.

        if idx < total_numbers - 1:  # Not the rightmost number.
            even_jump_idx = next_non_greater_indices[idx]
            if even_jump_idx is None:
                even_jump_availability.update({idx: False})

            else:
                even_jump_availability.update(
                    {idx: odd_jump_availability[even_jump_idx]}
                )

            odd_jump_idx = next_non_smaller_indices[idx]
            if odd_jump_idx is None:
                odd_jump_availability.update({idx: False})

            else:
                odd_jump_availability.update(
                    {idx: even_jump_availability[odd_jump_idx]}
                )
                if odd_jump_availability[idx]:
                    total_good_starting_indices += 1

    return total_good_starting_indices
