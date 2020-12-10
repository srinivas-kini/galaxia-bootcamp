import csv


def remove_spaces(ls):
    return [elem.strip() for elem in ls]


with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # The iterator skips the first line (i.e the headers)
    for line in csv_reader:
        print(line)

# Copy the contents of this csv into a new one with a different delimiter
with open('data.csv', 'r') as org_csv:
    csv_reader = csv.reader(org_csv)  # if the csv file is separated by '-', add delimiter = '-'
    with open('copy_data.csv', 'w') as new_csv: # creates a new file
        csv_writer = csv.writer(new_csv, delimiter='-')  # \t for tabs
        for line in csv_reader: # get line from the first csv
            csv_writer.writerow(remove_spaces(line))
