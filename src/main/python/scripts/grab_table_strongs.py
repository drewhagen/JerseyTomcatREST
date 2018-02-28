'''
@date : 2.23.2018
@author : Drew Hagen
@script-reuse : SUBJECTIVE
@description : script for grabbing strongs out of an html table/html substring...
Specifically looking for data contained in strong tags.
'''

def getStrongs(html_file_path):
    strong_contents = []
    out_str = ""
    with open(html_file_path, 'rb+') as html_file:
        file_content = html_file.read()
        split_example = file_content.split("<strong>")
        for i in split_example:
            if(i.split("</strong>")[0]!="&nbsp;"):
                strong_contents.append(i.split("</strong>")[0])
    for content in strong_contents:
        out_str += content + ", "
    print out_str

def getPs(html_file_path):
    strong_contents = []
    out_str = ""
    with open(html_file_path, 'rb+') as html_file:
        file_content = html_file.read()
        split_example = file_content.split("<p>")
        for i in split_example:
            if (i.split("</p>")[0] != "&nbsp;"):
                strong_contents.append(i.split("</p>")[0])
    for content in strong_contents:
        out_str += content + ", "
    print out_str

def getSpans(html_file_path):
    strong_contents = []
    out_str = ""
    with open(html_file_path, 'rb+') as html_file:
        file_content = html_file.read()
        split_example = file_content.split("<span>")
        for i in split_example:
            if (i.split("</span>")[0] != "&nbsp;"):
                strong_contents.append(i.split("</span>")[0])
    for content in strong_contents:
        out_str += content + ", "
    print out_str