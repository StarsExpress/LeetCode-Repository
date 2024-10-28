
def find_uniqueness_median(numbers: list[int]) -> int:  # LeetCode Q.3134.
    """
    Array of uniqueness <= x: number of subarrays of uniqueness <= x = right idx + 1 - left idx.
    """
    total_numbers = len(numbers)
    total_subarrays = (1 + total_numbers) * total_numbers // 2
    median = (total_subarrays + 1) // 2  # 2n + 1: (n + 1)th; 2n: nth.

    min_answer, max_answer = 1, total_numbers // 2
    count = 0  # Number of subarrays with distinction <= (min answer + max answer) // 2.
    window_occurrences, window_distinction = dict(), 0

    while min_answer <= max_answer:
        mid_answer = (min_answer + max_answer) // 2

        count -= count  # Reset before counting.
        window_occurrences.clear()
        window_distinction -= window_distinction

        left_idx, right_idx = 0, 0
        while right_idx < total_numbers:
            if numbers[right_idx] not in window_occurrences.keys():
                window_distinction += 1
                window_occurrences.update({numbers[right_idx]: 0})
            window_occurrences[numbers[right_idx]] += 1

            while window_distinction > mid_answer:
                window_occurrences[numbers[left_idx]] -= 1
                if window_occurrences[numbers[left_idx]] == 0:
                    window_distinction -= 1
                    del window_occurrences[numbers[left_idx]]

                left_idx += 1

            count += right_idx + 1 - left_idx
            right_idx += 1

        if count >= median:
            max_answer = mid_answer - 1
            continue
        min_answer = mid_answer + 1

    return min_answer
