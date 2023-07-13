import os
from datetime import datetime, timedelta

def search_files(start_time, end_time, folder_path):
    start_datetime = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
    end_datetime = datetime.strptime(end_time, "%Y-%m-%d %H:%M")

    matched_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            
            if start_datetime <= file_modified_time <= end_datetime:
                matched_files.append(file_path)

    return matched_files

# Example usage
start_time = "2021-12-02 00:00"
end_time = "2021-12-02 23:00"
folder_path = r"C:\Users\Saipunith\Desktop\google fonts\DeepLearn"

matched_files = search_files(start_time, end_time, folder_path)

print("Matched files:")
for file in matched_files:
    print(file)
