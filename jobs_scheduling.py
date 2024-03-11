from config import DATA_FOLDER_PATH
import os
import pandas as pd


def read_jobs(diff_mode=True):  # Job priority: calculated by either weight - length or weight / length.
    file_path = os.path.join(DATA_FOLDER_PATH, 'jobs.txt')
    with open(file_path, 'r') as file:
        jobs = file.read().splitlines()[1:]  # Skip the 1st line that isn't related to job's weight & length.
        file.close()

    columns = ['weight', 'length']
    if diff_mode:
        columns.append('diff')

    else:
        columns.append('ratio')

    jobs_df_values = []
    for job in jobs:
        jobs_list = job.lstrip().rstrip().split(' ')  # Remove boundary spaces and split by middle space.
        weight, length = int(jobs_list[0]), int(jobs_list[1])  # 1st item: weight; 2nd item: length.
        job_priority = weight - length if diff_mode else weight / length
        jobs_df_values.append([weight, length, job_priority])

    jobs_df = pd.DataFrame(jobs_df_values, columns=columns)
    jobs_df.sort_values(by=[columns[-1], 'weight'], ascending=[False, False], inplace=True)
    jobs_df.reset_index(drop=True, inplace=True)
    del file, file_path, job, jobs, jobs_list, job_priority, jobs_df_values
    return jobs_df


def compute_weighted_time(diff_mode=True):
    jobs_df = read_jobs(diff_mode)
    return sum(jobs_df['weight'] * jobs_df['length'].cumsum())


if __name__ == '__main__':
    import time

    start_time = time.time()
    print(f'Weighted scheduling time: {compute_weighted_time(False)}')
    end_time = time.time()
    print(f'\nRun Time: {str(round(end_time - start_time))} seconds.')
