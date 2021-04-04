import os


def read_doc_list(file_name):
    doc = []
    for line in open(file_name, 'r').readlines():
        doc.append(line)
    return doc


csv_data_file = 'devices.csv'
csv_data = read_doc_list(csv_data_file)
headers = csv_data[0].rstrip('\n').split(',')
print(headers)
