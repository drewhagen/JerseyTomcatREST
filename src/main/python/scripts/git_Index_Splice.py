import os.path

'''
A script that will append the filetype of a filepath into a new column in CSV
10.24.2017
Drew Hagen
'''


def splice_off_index(cell):
    return cell[50:]



def fileTypeToColumn(rcfile, wcfile):
    if os.path.isfile(rcfile) & os.path.isfile(wcfile):
        import csv
        with open(rcfile, 'rb') as infile:
            with open(wcfile, 'wb') as outfile:
                reader = csv.reader(infile, delimiter=",")
                writer = csv.writer(outfile, delimiter=",")
                for row in reader:
                    new_references = splice_off_index(row[7])
                    row.append(new_references)
                    writer.writerow(row)