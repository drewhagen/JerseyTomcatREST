import os, csv


def cut_Duplicate_In_Line(file_in):
    if os.path.isfile(file_in):
        with open(file_in, 'rb') as read_file:
            with open(file_in, 'wb') as write_file:
                lines = [line.rstrip('\n') for line in read_file]
                lines = lines[2:]
                for line in lines:
                    print line
