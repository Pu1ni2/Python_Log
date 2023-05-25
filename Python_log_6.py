import re

def generate_task_name(log_file_name):
    # Extract session ID and timestamp using regular expressions
    pattern = r'.*_(\d+)_([0-9]{8}_[0-9]{6})\.log'
    match = re.match(pattern, log_file_name)
    
    if match:
        session_id = match.group(1)
        timestamp = match.group(2)
        
        # Generate task name using session ID and timestamp
        task_name = f"Task_{session_id}_{timestamp}"
        return task_name
    else:
        print("Invalid log file name format")
        return None

# Example usage
log_file_name = "logfile_12345_20210520_153000.log"
task_name = generate_task_name(log_file_name)
print(task_name)
