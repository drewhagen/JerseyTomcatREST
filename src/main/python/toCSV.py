import os.path


'''
A script that will convert each single line from a .txt file to a row in .csv file.
10.23.2017
Drew Hagen
'''


def eachline(tf):  #tf -> txt file, cf -> csv file
    if os.path.isfile(tf):
        thisfile = open(tf, 'r')
        for eachline in thisfile:
            print eachline
    else:
        print "not a file"


def linetorow(tf, cf):
    if os.path.isfile(tf):
        thisfile = open(tf, 'r')
        import csv
        with open(cf, 'wb') as csvfile:
            portalwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            for eachline in thisfile:
                if eachline!="":
                    portalwriter.writerow(eachline)
    else:
        print "not a file"