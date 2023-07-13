import os
import datetime

def get_files_in_range(start_datetime, end_datetime, folder_path):
    files_in_range = []
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if start_datetime <= file_time <= end_datetime:
                files_in_range.append(file_path)
    return files_in_range

# Input date and time range
start_date = input("Enter start date (YYYY-MM-DD): ")
start_time = input("Enter start time (HH:MM): ")
end_date = input("Enter end date (YYYY-MM-DD): ")
end_time = input("Enter end time (HH:MM): ")

# Convert input to datetime objects
start_datetime = datetime.datetime.strptime(start_date + " " + start_time, "%Y-%m-%d %H:%M")
end_datetime = datetime.datetime.strptime(end_date + " " + end_time, "%Y-%m-%d %H:%M")

# Folder path to search
folder_path = "/path/to/folder"  # Replace with the actual folder path

# Get files within the specified range
files_in_range = get_files_in_range(start_datetime, end_datetime, folder_path)

# Print the found files
print("Files within the specified range:")
for file_path in files_in_range:
    print(file_path)
