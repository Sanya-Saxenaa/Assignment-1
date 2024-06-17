#To read and print values from csv file
import csv
with open(q15.csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)
