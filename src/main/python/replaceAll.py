'''
@date : 12.13.2017
@author : Drew Hagen
@script : SUBJECTIVE
@description : A script that will make a string more html friendly, replacing all instances
of <, >, ? and &.
@param : .json file
@return : modified .json file
'''
import os

def makeFileHTMLFriendly(file_in, file_out):
    if os.path.isfile(file_in) & os.path.isfile(file_out):
        with open(file_in, "rb") as read_file:
            with open(file_out, "wb") as write_file:
                contents = read_file.read()
                # contents = contents.replace('&', "&amp;")
                # contents = contents.replace('<', "&lt;")
                # contents = contents.replace('>', "&gt;")
                # contents = contents.replace('?', "->")
                contents = contents.replace("undefined	", "")
                write_file.write(contents)

