
def _binary_search(job: int, sorted_jobs: list[int], size: int):
    if size == 0:
        return 0

    back_idx, front_idx = 0, size - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_jobs[mid_idx] <= job:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of jobs <= target job, implying insertion idx.


def find_max_profits(difficulty: list[int], profit: list[int], worker: list[int]) -> int:  # LeetCode Q.826.
    total_jobs, sorted_jobs, profits = 0, [], []
    for job_difficulty, job_profit in zip(difficulty, profit):
        insertion_idx = _binary_search(job_difficulty, sorted_jobs, total_jobs)
        sorted_jobs.insert(insertion_idx, job_difficulty)
        profits.insert(insertion_idx, job_profit)
        total_jobs += 1

    # Turn profits array into array of each max of prefix profits subarray[:ith idx].
    for idx, profit in enumerate(profits):
        if idx > 0 and profits[idx - 1] > profit:  # Adjustment starts from 2nd profit.
            profits[idx] = profits[idx - 1]

    max_profits = 0
    for ability in worker:
        insertion_idx = _binary_search(ability, sorted_jobs, total_jobs)
        if insertion_idx > 0:
            max_profits += profits[insertion_idx - 1]

    return max_profits
