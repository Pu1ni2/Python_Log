import os

import datetime

folder_path = "/path/to/folder"

latest_file = None

latest_time = datetime.datetime.min

for filename in os.listdir(folder_path):

    if filename.endswith('.csv'): #you can change the extension as per your need

        file_time = datetime.datetime.strptime(filename[-16:], '%Y_%m_%d_%H_%M')

        if file_time > latest_time:

            latest_time = file_time

            latest_file = filename

print("Latest file is:", latest_file)

