import os

def eachline(tf):  #tf -> txt file, cf -> csv file
    if os.path.isfile(tf):
        thisfile = open(tf, 'r')
        for eachline in thisfile:
            print eachline[2:]
    else:
        print "not a file"