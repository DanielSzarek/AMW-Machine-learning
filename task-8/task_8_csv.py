import csv
import pandas as pd

counter = 1


def new_task():
    global counter
    print(f"\n{counter}. ========================================================")
    counter += 1


new_task()
with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names: {", ".join(row)}')
        else:
            print(f'\t{row[0]} from {row[1]} department, get birthday in: {row[2]}')
        line_count += 1
    print(f"Processed {line_count} lines")

new_task()
with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, get birthday in: {row["birthday_month"]}.')
        line_count += 1
    print(f"Processed {line_count} lines")

new_task()
with open('sports.csv', mode='w') as sport_file:
    sport_writer = csv.writer(sport_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    sport_writer.writerow(['tennis', 1])
    sport_writer.writerow(['football', 11])
    sport_writer.writerow(['box', '1'])

new_task()
with open('sports2.csv', mode='w') as sport2_file:
    fieldnames = ['sport_name', 'players']
    sport_writer = csv.DictWriter(sport2_file, fieldnames=fieldnames)

    sport_writer.writeheader()
    sport_writer.writerow({'sport_name': 'basketball', 'players': 5})
    sport_writer.writerow({'sport_name': 'football', 'players': 11})

new_task()
data_frame = pd.read_csv('hrdata.csv')
print(data_frame)

data_frame_index = pd.read_csv('hrdata.csv', index_col='Name')
print(data_frame_index)

df = pd.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
print(df)

df = pd.read_csv('hrdata.csv',
                 index_col='Employee',
                 parse_dates=['Hired'],
                 header=0,
                 names=['Employee', 'Hired', 'Salary', 'Sick Days'])
print(df)

df = pd.read_csv('hrdata.csv',
                 index_col='Employee',
                 parse_dates=['Hired'],
                 header=0,
                 names=['Employee', 'Hired', 'Salary', 'Sick Days'])
df.to_csv('hrdata_modified.csv')
