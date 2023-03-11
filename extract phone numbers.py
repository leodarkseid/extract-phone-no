import pandas as pd
import re

# Define a regular expression to match phone numbers
phone_regex = r'(\+?\d{2})?(\d{10})'

# Read the CSV file into a pandas dataframe
df = pd.read_csv('input.csv')

# Create an empty list to store the phone numbers
phone_numbers = []

# Iterate over each row in the dataframe
for index, row in df.iterrows():
    # Extract phone numbers using the regular expression
    matches = re.findall(phone_regex, row['text'])
    # Flatten the matches list and filter out empty strings
    matches = [phone_number[0] + phone_number[1] for phone_number in matches if phone_number != ('', '')]
    # Append the phone numbers to the list
    phone_numbers += matches

# Convert the list of phone numbers into a pandas dataframe
phone_df = pd.DataFrame({'phone': phone_numbers})

# Write the phone numbers dataframe to an Excel sheet
phone_df.to_excel('output.xlsx', index=False)
