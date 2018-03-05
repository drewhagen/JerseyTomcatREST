import os.path

'''
A script that will append the filetype of a filepath into a new column in CSV
10.24.2017
Drew Hagen
'''


def gettype(file_path):
    file_type=" "
    for char in file_path[::-1]:
        file_type = char + file_type
        if char == ".":
            break
    return file_type


def fileTypeToColumn(rcfile, wcfile):
    if os.path.isfile(rcfile) & os.path.isfile(wcfile):
        import csv
        with open(rcfile, 'rb') as infile:
            with open(wcfile, 'wb') as outfile:
                reader = csv.reader(infile, delimiter=",")
                writer = csv.writer(outfile, delimiter=",")
                for row in reader:
                    this_row_file_type = gettype(row[0])
                    row.append(this_row_file_type)
                    writer.writerow(row)