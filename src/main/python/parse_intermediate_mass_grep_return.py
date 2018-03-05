'''
@date : 11.17.2017
@author : Drew Hagen
@script : SUBJECTIVE
@description : A script that will crawl through a messy plain text file of poorly coordinated grep output.
@param : .txt file, CSV file
@return : None BUT @procedure : modified CSV
@DEPENDENCIES: python's CSV

start function(in_txt, out_csv):
        if os.path.isfile(in_txt) & os.path.isfile(out_csv):
        with open(in_txt, 'rb') as read_file:
            with open(out_csv, 'wb') as write_file:
                reader = read_file.read()
                writer = csv.writer(write_file, delimiter=",")
                for row in reader:



'''

import csv
import os

def function(in_txt, in_csv, out_csv):
    if os.path.isfile(in_txt) & os.path.isfile(out_csv):
        with open(in_txt, 'rb') as read_file:
            with open(in_csv, 'rb') as read_csv:
                with open(out_csv, 'rwb') as write_file:
                    reader2 = csv.reader(read_csv, delimiter=",")
                    writer = csv.writer(write_file, delimiter=",")
                    for row in reader2:

