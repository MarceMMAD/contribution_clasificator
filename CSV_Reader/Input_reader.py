import csv

def csv_data_extract(file_name):
    csv_file = open(file_name,'r')
    csv_reader = csv.reader(csv_file,delimiter=';')
    submission_list  =[]
    for row in csv_reader:
        submission_text = str(row[0]) + ' ' + str(row[1])
        submission_category = row[2]
        submission = [submission_text, submission_category]
        submission_list.append(submission)
    return submission_list