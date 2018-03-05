'''
@date : 12.6.2017
@author : Drew Hagen
@script : OBJECTIVE
@description : A script that simply converts CSV into json.
@param : CSV file
@return : json file
@DEPENDENCIES: python's json module
'''
import csv
import os
import json


def convert(in_csv, out_json):
    if os.path.isfile(in_csv) & os.path.isfile(out_json):
        with open(in_csv, 'rb') as read_csv:
            with open(out_json, 'wb') as write_json:
                reader = csv.DictReader(read_csv)
                for row in reader:
                    row = list_of_new_format(row)
                    json.dumps(row, write_json)
                    write_json.write('\n')


def list_of_new_format(row):
    for val in row:
        val = val.encode('utf-8').strip()
    return row