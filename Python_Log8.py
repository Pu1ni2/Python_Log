import re

log_file_name = "sesrfj_rjddkdk_djdjd_djdk_jkr_02_12677_2023-05-14.txt"
pattern = r"(.+)_\d{2}_\d+_\d{4}-\d{2}-\d{2}\.txt"

match = re.match(pattern, log_file_name)
if match:
    task_name = match.group(1)
    print(task_name)
else:
    print("No match found.")
