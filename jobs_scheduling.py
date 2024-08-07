import os
import pandas as pd
from config import DATA_FOLDER_PATH


def read_jobs(diff_mode=True):
    """Job priority calculated by either weight - length or weight / length."""
    file_path = os.path.join(DATA_FOLDER_PATH, "jobs.txt")
    with open(file_path, "r") as file:
        jobs = file.read().splitlines()[1:]  # 1st line unrelated to job weight & length.
        file.close()

    columns = ["weight", "length"]
    if diff_mode:  # Job priority calculated by weight - length.
        columns.append("diff")

    else:  # Job priority calculated by weight / length.
        columns.append("ratio")

    jobs_df_values = []
    for job in jobs:  # Remove edge spaces and split by middle space.
        weight, length = job.lstrip().rstrip().split(" ")  # 1st item: weight; 2nd item: length.
        weight, length = int(weight), int(length)
        job_priority = weight - length if diff_mode else weight / length
        jobs_df_values.append([weight, length, job_priority])

    jobs_df = pd.DataFrame(jobs_df_values, columns=columns)
    jobs_df.sort_values(by=[columns[-1], "weight"], ascending=[False, False], inplace=True)
    jobs_df.reset_index(drop=True, inplace=True)
    return jobs_df


def compute_weighted_time(diff_mode=True):
    jobs_df = read_jobs(diff_mode)
    return sum(jobs_df["weight"] * jobs_df["length"].cumsum())
