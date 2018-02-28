import os
import csv

'''
A script that will empty a CSV file, so to speak.
In reality, it replaces a CSV file with an empty file .csv
10.26.2017
Drew Hagen
'''


def reset(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
        with open(file_path, 'w+'):
            print(file_path + " should be reset.")
