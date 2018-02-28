import os.path
import csv
'''
A script that will slice out alternating white space in CSV files, hopefully
In our Excel spreadsheet, all strings were formatted to have alternating spaces. WE DON'T LIKE THIS!
First Column: every even character has a space in it. Other Columns: Just get rid of whitespace altogether
10.24.2017
Drew Hagen
SUCCESSFUL SCRIPT! :)
'''


def begone(in_file, out_file):
    if os.path.isfile(in_file) & os.path.isfile(out_file):
        with open(in_file, 'rb') as readfile:
            with open(out_file, 'wb') as writefile:
                reader = csv.reader(readfile, delimiter=",")
                writer = csv.writer(writefile, delimiter=",")
                for row in reader:  # for each row, [0]->len
                    i = 0
                    values = []
                    while i < 4:
                        this_cell = row[i]
                        j = 0
                        new_cell = None
                        # while j < len(this_cell):
                        #     if this_cell[j] != " ":
                        #         new_cell = new_cell+this_cell[j]
                        #     j = j + 1
                        if i == 0:
                            for char in this_cell: # different algorithms for file path (first) column
                                # this one will delete alternating characters, which appears to be the unwanted spaces
                                if j == 0:
                                    new_cell = char
                                if (j != 0) & (j % 2 == 0):
                                    new_cell += char
                                j = j + 1
                        else: # the algorithm for every other column
                            # very simply, this will clear out whitespace. The first row must maintain some whitespace
                            for char in this_cell:
                                if char != ' ':
                                    try:
                                        new_cell += char
                                    except TypeError:
                                        new_cell = char
                        values.append(new_cell)
                        i = i + 1
                    writer.writerow(values)
