# First we'll import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Reading using CSV module

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    num_month = 0
    net_total = 0
    for row in csvreader:
       
       num_month += 1
       net_total = net_total + int(row[1])

    print(f"Total Months: {num_month}")
    print(f"Total:${net_total}")
    

