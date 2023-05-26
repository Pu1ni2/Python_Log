import os

def extract_task_name(file_name):
    # Remove the file extension
    file_name = os.path.splitext(file_name)[0]

    # Split the file name by underscore
    parts = file_name.split('_')

    # Remove the last two parts (session ID and timestamp)
    task_name = '_'.join(parts[:-2])

    return task_name

# Example usage
log_file_name = 'sesrfj_rjddkdk_djdjd_djdk_jkr_02_12677_2023-05-14.txt'
task_name = extract_task_name(log_file_name)
print(task_name)
