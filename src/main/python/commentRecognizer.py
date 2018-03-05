import os.path
import csv
import math
import scanner.c_parser
import HTMLParser

import src.emptyCSV
import src.unixPathToWindows

'''
A script that will recognize comments in a code paradigm within a file.
What denotes comments is dependent on the language of the code.
10.25.2017
Drew Hagen
'''


def get_frequency(term, filepath, scanline): #intention: to return frequency per line
    filepath = filepath[1:]
    filepath = os.path.abspath("C:\Users\drew.hagen\workspace\campus" + filepath)
    if os.path.isfile(filepath):
        with open(filepath, 'rb') as file:
            i = 1
            for line in file:
                if i == int(scanline):
                    count = count = line.count(term)
                    return count
                i += 1
            return file


#def count_occurrences(term, line):
    #count = line.count(term)
    #return count


def put_frequency(csv_file_in, csv_file_out):
    if os.path.isfile(csv_file_in) & os.path.isfile(csv_file_out):
        with open(csv_file_in, 'rb') as read_file:
            # src.emptyCSV.reset(csv_file_out)
            with open(csv_file_out, 'wb') as write_file:
                reader = csv.reader(read_file, delimiter=",")
                writer = csv.writer(write_file, delimiter=",")
                for row in reader:
                    frequency = get_frequency(row[2], row[0], row[1])
                    row.append(frequency)
                    writer.writerow(row)


# NEEDS FIXES
# def new_frequency(term, csv_file_in, csv_file_out):
#     if os.path.isfile(csv_file_in) & os.path.isfile(csv_file_out):
#         with open(csv_file_in) as read_file:
#             with open(csv_file_out) as write_file:
#                 reader = csv.reader(csv_file_in, delimiter=",")
#                 writer = csv.writer(csv_file_out, delimiter=",")
#                 for row in reader:
#                     frequency = get_frequency(term, row[0], row[1])
#                     row.append(frequency)
#                     writer.writerow(row)

def unixToWin(filepath):
    filepath = filepath[1:]
    filepath = os.path.abspath("C:\Users\drew.hagen\workspace\campus" + filepath)
    return filepath


def checkeach(csv_file_in, csv_file_out):
    if os.path.isfile(csv_file_in) & os.path.isfile(csv_file_out):
        with open(csv_file_in, 'rb') as read_file:
            with open(csv_file_out, 'wb') as write_file:
                reader = csv.reader(read_file, delimiter=",")
                writer = csv.writer(write_file, delimiter=",")
                #### TODO: CHANGE THE LOGIC BELOW!!!
                for row in reader:
                   try:
                        commentLines = search(row[0], int(row[1]), row[3])
                        row.append(commentLines)
                        writer.writerow(row)
                   except ValueError:
                       print "probably a string can't convert into an int at " + row[0] + " skipping . . ."
                       writer.writerow(row)


def search(filepath, scanline, filetype):
    filepath = unixToWin(filepath)
    if filetype == ".java":
        return scan_java(filepath, scanline)
    elif filetype == ".js":
        return scan_js(filepath, scanline)
    elif filetype == ".css" or filetype == ".scss":
        return scan_css(filepath, scanline)
    elif filetype == ".groovy":
        return scan_groovy(filepath, scanline)
    elif filetype == ".gradle":
        return scan_graddle(filepath, scanline)
    else:
        return " "

# Java Comments
def scan_java(_file, scanline):
    result = ""
    try:
        comments = scanner.c_parser.extract_comments(_file)
        for comment in comments:
            discom = comment.text()
            if "portal" in discom.lower():
                #print comment.text()
                if abs(scanline - comment.line_number()) < 2:
                    result += "yes"
                #print comment.is_multiline()
    except scanner.c_parser.UnterminatedCommentError:
        pass
    return result


# Javascript Comments
def scan_js(_file, scanline):
    result = ""
    try:
        comments = scanner.c_parser.extract_comments(_file)
        for comment in comments:
            discom = comment.text()
            if "portal" in discom.lower():
                # print comment.text()
                if abs(scanline - comment.line_number()) < 2:
                    result += "yes"
                    # print comment.is_multiline()
    except scanner.c_parser.UnterminatedCommentError:
        pass
    return result


# CSS Comments
def scan_css(_file, scanline):
    result = ""
    try:
        comments = scanner.c_parser.extract_comments(_file)
        for comment in comments:
            discom = comment.text()
            if "portal" in discom.lower():
                # print comment.text()
                if abs(scanline - comment.line_number()) < 2:
                    result += "yes"
                    # print comment.is_multiline()
    except scanner.c_parser.UnterminatedCommentError:
        pass
    return result


# gradle Comments
def scan_graddle(_file, scanline):
    result = ""
    try:
        comments = scanner.c_parser.extract_comments(_file)
        for comment in comments:
            discom = comment.text()
            if "portal" in discom.lower():
                # print comment.text()
                if abs(scanline - comment.line_number()) < 2:
                    result += "yes"
                    # print comment.is_multiline()
    except scanner.c_parser.UnterminatedCommentError:
        pass
    return result


# groovy Comments
def scan_groovy(_file, scanline):
    result = ""
    try:
        comments = scanner.c_parser.extract_comments(_file)
        for comment in comments:
            discom = comment.text()
            if "portal" in discom.lower():
                # print comment.text()
                if abs(scanline - comment.line_number()) < 2:
                    result += "yes"
                    # print comment.is_multiline()
    except scanner.c_parser.UnterminatedCommentError:
        pass
    return result

'''
class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        print "Data     :" + data
        print self.getpos()
'''


# fop Comments
#def scan_fop():


# html Comments
# def scan_html(data, scanline):


# icml Comments
#def scan_icml():


# jsp Comments
#def scan_jsp():


# sql Comments
#def scan_sql():


# XML Comments
#def scan_xml():


# xsd (XML schema) Comments
#def scan_xsd():


# Property Comments?
#def scan_props():
    

# SPECIAL CASES:
# zip, txt, jar

# UNKNOWN CASES:
# .dic, .dev, .csv, .iws, .md, .map, .json


'''elif filetype == ".html":
    with open(filepath, 'rb') as source:
        data = source.read()
        return scan_html(data, scanline)'''