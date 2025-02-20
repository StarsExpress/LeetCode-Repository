import os
import heapq
from config import DATA_FOLDER_PATH


def read_jobs(diff_mode=True) -> list[list[int | float]]:
    """Job priority calculated by either weight - length or weight / length."""
    file_path = os.path.join(DATA_FOLDER_PATH, "jobs.txt")
    with open(file_path, "r") as file:
        jobs = file.read().splitlines()[1:]  # 1st line unrelated to job weight & length.
        file.close()

    terms = ["weight", "length"]
    if diff_mode:  # Job priority calculated by weight - length.
        terms.append("diff")

    else:  # Job priority calculated by weight / length.
        terms.append("ratio")

    processed_jobs = []
    for job in jobs:  # Remove edge spaces and split by middle space.
        weight, length = job.lstrip().rstrip().split(" ")  # 1st item: weight; 2nd item: length.
        weight, length = int(weight), int(length)
        job_priority = weight - length if diff_mode else weight / length
        processed_jobs.append([weight, length, job_priority])

    return processed_jobs


def compute_weighted_time(diff_mode=True) -> int:
    jobs = read_jobs(diff_mode)
    max_heap = []
    for weight, length, job_priority in jobs:
        # Negate priority & weight to fit into max heap.
        heapq.heappush(max_heap, (-job_priority, -weight, length))

    weighted_time, cumulated_time = 0, 0
    while max_heap:
        _, weight, length = heapq.heappop(max_heap)
        cumulated_time += length
        weighted_time += (-weight) * cumulated_time  # Negate weight back to its original value.

    return weighted_time
