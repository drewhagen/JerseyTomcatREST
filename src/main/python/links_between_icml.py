import os.path
import csv
'''
A script that will take a list of hyperlink markup docs with known front-end navigation (exist in a nav bar index)
and search them for references to hyperlink markup docs without known navigation.
11.14.2017
Drew Hagen
'''

def has_UI_test_distribute(in_csv, out_csv):
    files_with_UI_path = []
    deep_files = []
    if os.path.isfile(in_csv) & os.path.isfile(out_csv):
        with open(in_csv, 'rb') as read_file:
            reader = csv.reader(read_file, delimiter=",")
            for row in reader:
                if (row[6] != "") & (row[6] is not None):
                    files_with_UI_path.append(row[0])
                else:
                    deep_files.append(row[0])
            reference_map = check_indexed_for_refs(files_with_UI_path, deep_files)
            print_list_of_refs(reference_map, in_csv, out_csv)


def check_indexed_for_refs(files_with_UI_path, deep_files):
    print "     running check_indexed_for_refs"
    index_to_deep = {}
    for dex_src_file in files_with_UI_path:
        with open(unixToWin(dex_src_file), 'r') as src_file:
            index_to_deep[dex_src_file] = []
            for deep_file in deep_files:
                chunk = deep_file.split("/")
                last = len(chunk) - 1
                if chunk[last] in src_file.read():  # if file name only exists in contents of src_file
                    print "     Oh my gosh, it happened!"
                    list = index_to_deep.get(dex_src_file, default=[])
                    list.append(chunk[last])
                    index_to_deep[dex_src_file] = list
                else:
                    print chunk[last] + " is not in " + dex_src_file
    return index_to_deep


def print_list_of_refs(reference_map, in_csv, out_csv):
    if os.path.isfile(in_csv) & os.path.isfile(out_csv):
        with open(in_csv, 'rb') as read_file:
            with open(out_csv, 'wb') as write_file:
                reader = csv.reader(read_file, delimiter=",")
                writer = csv.writer(write_file, delimiter=",")
                for row in reader:
                    if row[0] in reference_map.keys():
                        list_of_ref = reference_map.get(row[0])
                        row.append(list_of_ref)
                        writer.writerow(row)
                    else:
                        row.append([])
                        writer.writerow(row)


def from_index_web_to_deep_web(in_csv, out_csv): # COMMENT THE HECK OUT OF THIS BECAUSE IT BECAME CONFUSING
    files_with_UI_path = []
    deep_files = []
    if os.path.isfile(in_csv) & os.path.isfile(out_csv):
        with open(in_csv, 'rb') as read_file:
            with open(out_csv, 'wb') as write_file:
                reader = csv.reader(read_file, delimiter=",")
                for row in reader:
                    if (row[6] != "") & (row[6] is not None):
                        file_path_wrapped_in_list = []
                        file_path_wrapped_in_list.append(row[0])
                        files_with_UI_path.append(file_path_wrapped_in_list)
                    else:
                        deep_files.append(row[0])
                print files_with_UI_path
                print deep_files
                for indexed_src_file in files_with_UI_path:
                    print "checking " + unixToWin(indexed_src_file[0]) + " ..."
                    with open(unixToWin(indexed_src_file[0]), 'r') as read_indexed_src:
                        print "     successfully opened!"
                        for unindexed_src_file in deep_files:
                            print "         looking for " + unindexed_src_file
                            data = unindexed_src_file.split("/")
                            last = len(data)
                            print "             " + data[last - 1]
                            if data[last - 1] in read_indexed_src.read():
                                print "             FOUND!"
                                indexed_src_file.append(data[last])

                reader = csv.reader(read_file, delimiter=",")
                writer = csv.writer(write_file, delimiter=",")



def unixToWin(filepath):
    filepath = os.path.abspath("C:\Users\drew.hagen\workspace\campus\\" + filepath)
    return filepath