'''
11.9.2017
Scripted version of a couple functions I'd like to test instead of OOP
from icml.py
'''
import os.path
import lxml
import csv

doc = lxml.etree.parse("C:\Users\drew.hagen\workspace\campus\database\\xml\update_CampusTool.xml")

print doc.xpath('//element[text()='+file_path+']')[0].text
print doc.xpath('//element[text()="A"]')[0].tag