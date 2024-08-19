
def find_kth_smallest_number(m: int, n: int, k: int):  # LeetCode Q.668.
    count = 0  # To be used during while loop.
    min_answer, max_answer = 1, m * n
    while min_answer < max_answer:  # Don't include equal sign!
        mid_answer = (min_answer + max_answer) // 2
        
        count -= count  # Reset before calculation.
        for num in range(1, m + 1):
            count += min(mid_answer // num, n)  # Take min of quotient and n.

        if count < k:
            min_answer = mid_answer + 1
            continue
        max_answer = mid_answer  # Don't minus 1!

    return min_answer
