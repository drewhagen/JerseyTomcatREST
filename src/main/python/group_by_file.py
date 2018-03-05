'''
@date : 12.15.2017
@author : Drew Hagen
@script : SUBJECTIVE
@description : Group rows by file duplicates, clump up line numbers, preserve the subset of line numbers which are comments
Original List -> Master List + One CSV for each FileType
'''
import os

def squash(in_csv):
    if os.path.isfile(in_csv):
        import csv
        with open(in_csv, 'rb') as infile:
            with open("masterlist.csv", 'wb+') as outfile:
                with open("totals.csv", 'wb+') as totals:
                    reader = csv.reader(infile, delimiter=",")
                    writer = csv.writer(outfile, delimiter=",")
                    totals_writer = csv.writer(totals, delimiter=",")
                    totals_info = {}
                    per_File_Dictionary = {}
                    per_Type_Dictionary = {}
                    for row in reader:
                        line_numbers = []
                        line_numbers.append(row[1])
                        value = [row[0], line_numbers, row[3]]
                        if row[0] in list(per_File_Dictionary.keys()): # we've seen this file before
                            value = per_File_Dictionary.get(row[0], "")
                            line_list = value[1]
                            line_list.append(row[1])
                            value[1] = line_list
                            per_File_Dictionary[row[0]] = value
                        else: # This is the first occurance in this line
                            per_File_Dictionary[row[0]] = value
                        if ("/" not in row[3]) & ("File Type" not in row[3]):
                            if row[3] in list(per_Type_Dictionary.keys()): #We've seen this file type before
                                files_of_this_type = per_Type_Dictionary.get(row[3], "")
                                if value not in files_of_this_type:
                                    files_of_this_type.append(value)
                                    totals_for_file_type = totals_info.get(row[3])
                                    totals_for_file_type[2] = totals_for_file_type[2] + 1
                                    totals_info[row[3]] = totals_for_file_type
                                per_Type_Dictionary[row[3]] = files_of_this_type
                            else: #this is a new filetype
                                list_of_files = []
                                list_of_files.append(value)
                                per_Type_Dictionary[row[3]] = list_of_files
                                totals_info[row[3]] = [row[3], 0, 0]
                            totals_for_file_type = totals_info.get(row[3])
                            totals_for_file_type[1] = totals_for_file_type[1] + 1
                            totals_info[row[3]] = totals_for_file_type
                    file_types = list(per_Type_Dictionary.keys())
                    for file_type in file_types:
                        s = str(file_type)[1:]+"_out.csv"
                        f = open(s, 'wb+')
                        w = csv.writer(f, delimiter=",")
                        v = per_Type_Dictionary.get(file_type, "")
                        for l in v:
                            w.writerow(l)
                        totals_writer.writerow(totals_info.get(file_type))
                    files = list(per_File_Dictionary.keys())
                    for file in files:
                        v = per_File_Dictionary.get(file, "")
                        writer.writerow(v)

