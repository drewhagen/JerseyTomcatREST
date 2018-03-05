import os.path
import csv
'''
A script that will look at XSL Includes inside markup source
in order to conclude an array of connected files within the repository
11.13.2017
Drew Hagen
'''


def log_related_files(in_csv, out_csv):
    if os.path.isfile(in_csv) & os.path.isfile(out_csv):
        with open(in_csv, 'rb') as read_file:
            with open(out_csv, 'wb') as write_file:
                reader = csv.reader(read_file, delimiter=",")
                writer = csv.writer(write_file, delimiter=",")
                for row in reader:
                    related_files = scan_relationships(row[0])
                    row.append(related_files)
                    iframes = scan_for_iframes(row[0])
                    row.append(iframes)
                    writer.writerow(row)


def scan_relationships(icml_file):
    related_files = []
    icml_file = unixToWin(icml_file)
    print icml_file
    if os.path.isfile(icml_file):
        print "isFile is true!"
        with open(icml_file, 'r') as read_file:
            print "opened" + icml_file
            for line in read_file:
                if "xsl:include" in line:
                    print "xsl include found"
                    data = line.split("\"")
                    print data
                    related_files.append(data[1])
            return related_files


def scan_for_iframes(icml_file):
    related_files = []
    icml_file = unixToWin(icml_file)
    print icml_file
    if os.path.isfile(icml_file):
        print "isFile is true!"
        with open(icml_file, 'r') as read_file:
            print "opened" + icml_file
            for line in read_file:
                if "iframe" in line:
                    print "iframe found"
                    data = line.split("\"")
                    print data
                    src = ""
                    i = 0
                    for element in data:
                        if "src=" in element:
                            src = data[i+1]
                        i = i + 1
                    related_files.append(src)
            return related_files


def unixToWin(filepath):
    filepath = os.path.abspath("C:\Users\drew.hagen\workspace\campus\\" + filepath)
    return filepath