import pandas as pd
import re

# read the excel file into a pandas dataframe
df = pd.read_excel('error_lookup.xlsx')

# define the regular expression pattern to match the error message
pattern = r'^\d{2}:\d{2}:\d{2} Error'

# open the log file
with open('log.txt', 'r') as f:
    # iterate over each line in the file
    for line in f:
        # check if the line matches the pattern
        if re.match(pattern, line):
            # extract the error message
            error_message = line.split(' ', 1)[1].strip()
            # look up the error message in the dataframe
            result = df[df['Error Message'].str.contains(error_message)]
            # print the corresponding column value if found
            if len(result) > 0:
                print(result.iloc[0]['Column Name'])
