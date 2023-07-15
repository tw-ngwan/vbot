#TODO: Add the code from GPT

import pandas as pd 

csv_path = 'trip-records.csv'

df = pd.read_csv(csv_path)

# Convert date columns to datetime
df['Start Date'] = pd.to_datetime(df['Start Date'], dayfirst=True)
df['End Date'] = pd.to_datetime(df['End Date'], dayfirst=True)

# Strip string from location 
df['Location'] = df['Location'].apply(str.strip)
df['Index'] = 161 - df['Index']
df = pd.read_csv(csv_path)

# Convert date columns to datetime
df['Start Date'] = pd.to_datetime(df['Start Date'], dayfirst=True)
df['End Date'] = pd.to_datetime(df['End Date'], dayfirst=True)

# Strip string from location 
df['Location'] = df['Location'].apply(str.strip)
df = df.sort_values(by='Start Date', ascending=False)

df['Start Date'] = df['Start Date'].dt.strftime('%d/%m/%Y')

df['End Date'] = df['End Date'].dt.strftime('%d/%m/%Y')
report = [] 
# Iterate over each row in the DataFrame
for _, row in df.iterrows():
    report.append("Trip Number: {}".format(row['Index']))
    report.append("Location: {}".format(row['Location']))
    report.append("Start Date: {}".format(row['Start Date']))
    report.append("End Date: {}".format(row['End Date']))
    report.append("Duration (days): {}".format(row['Duration (days)']))
    report.append("Purpose of Trip: {}".format(row['Purpose of Trip']))
    report.append("")  # Add an empty line between rows

report_txt = '\n'.join(report)
with open('report.txt', 'w') as f:
    f.write(report_txt)
    