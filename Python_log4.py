import re

def generate_task_name(log_file_name):

    # Extract session ID and timestamp from the log file name

    pattern = r'.*_(\d+)_(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})\.log'

    match = re.match(pattern, log_file_name)

    if match:

        session_id = match.group(1)

        timestamp = match.group(2)

        # Generate task name or file name

        task_name = f"Task_{session_id}_{timestamp}"

        return task_name

    else:

        return None  # File name format doesn't match the expected pattern

# Example usage

log_file_name = "logfile_12345_2023-05-24_10-15-30.log"

task_name = generate_task_name(log_file_name)

print(task_name)

