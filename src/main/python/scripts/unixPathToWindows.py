import os.path

'''
Simple script that changes the format of a unix file path into Windows file path
10.25.2017
Drew Hagen
'''


def convert(file_path):
    for i, char in enumerate(file_path):
        if char == '/':
            file_path[i] = '\\'
    return file_path
