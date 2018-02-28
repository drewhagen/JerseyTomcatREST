'''
@date : 1.31.2018
@author : Drew Hagen
@script-reuse : OBJECTIVE
@description : A robust script that can parse data from HTML tables in various ways, returning different data types
such as lists and dictionaries, and passing in rows, columns
'''

from BeautifulSoup import BeautifulSoup as BSHTML

class table_parser:
    html_file = None

    def __init__(self, html_file):
        print self.html_file
        self.html_file = open(html_file, "r")
        print self.html_file


    def header_for_column(self, header): # pass in a header name to return list of values in column matching that header
        BS = BSHTML(self.html_file)
        theaders = BS.find_all('th')

        count = 0
        index_of_interest = None
        data = []

        for theader in theaders:
            inner = theader.get_text()
            if (inner == header):
                index_of_interest = count
            count = count + 1

        rows = BS.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            for index, column in enumerate(cols):
                if(index == index_of_interest):
                    data.append(column.get_text())

        print data
        return data


