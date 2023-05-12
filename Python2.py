import pandas as pd

# Read in the Excel file and store it as a pandas dataframe
df = pd.read_excel('error_data.xlsx')

# Define the function to perform the lookup
def lookup_error(error):
    # Find the row in the dataframe where the data column is a substring of the error
    row = df[df['Data'].apply(lambda x: x in error)].iloc[0]
    # Return the corresponding column value from that row
    return row['Corresponding Column']

# Example usage
error = '2023-05-12 14:56:23 Error: Unable to connect to server'
corresponding_column = lookup_error(error)
print(corresponding_column)
