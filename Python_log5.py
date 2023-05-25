import re

def extract_task_name(log_file_name):

    pattern = r'^([\w_]+)_[\d-]+\.txt$'

    match = re.match(pattern, log_file_name)

    if match:

        return match.group(1)

    else:

        return None

# Example usage

log_file_name = "sesrfj_rjddkdk_djdjd_djdk_jkr_12038_02_2023-05-14.txt"

task_name = extract_task_name(log_file_name)

print(task_name)
