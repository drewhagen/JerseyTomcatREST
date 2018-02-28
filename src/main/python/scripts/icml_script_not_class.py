'''
11.9.2017
Scripted version of a couple functions I'd like to test instead of OOP
from icml.py
'''
import os.path
import xml.etree.ElementTree as ET
import csv
import lxml.etree


def get_line_occur(row):
    line_occur = [int(s) for s in row[1].split() if s.isDigit()]
    return line_occur


def search_element(file_path):
    x_path = []
    nav_str = 'Sidebar'
    xml_tree = lxml.etree.parse("C:\Users\drew.hagen\workspace\campus\database\\xml\update_CampusTool.xml")
    root = xml_tree.getroot()
    with open('foo.txt', 'w') as write_file:
        for elem in root.iter():
            url = elem.get('url', None)
            if url is not None:
                if file_path in url:
                    x_path.append(elem.get('name', None))
                    p = elem.getparent()
                    while p.getparent() is not None:
                        x_path.append(p.get('name', None))
                        p = p.getparent()
                    while (len(x_path) > 0):
                        nav_str += " -> " + x_path.pop()
                    return nav_str


def get_x_path_str(x_path):
    x_path_str = ""
    if x_path is not None:
        for x in x_path:
            x_path_str += " -> " + x.get('name', default="")
    return x_path_str


def add_nav_CSV(csv_file_in, csv_file_out):
    if os.path.isfile(csv_file_in) & os.path.isfile(csv_file_out):
        with open(csv_file_in, 'rb') as read_file:  # [1]
            with open(csv_file_out, 'wb') as write_file:
                reader = csv.reader(read_file, delimiter=",")   # [2]
                writer = csv.writer(write_file, delimiter=",")
                for row in reader:
                    nav_string = (search_element(row[0]))
                    row.append(nav_string)
                    writer.writerow(row)

