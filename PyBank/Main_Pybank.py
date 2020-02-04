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
   profit_col = []
   change_col = []
  
   for row in csvreader:
      
      num_month += 1
      net_total = net_total + int(row[1])
      profit_col.append(row[1])

   print(f"Total Months: {num_month}")
   print(f"Total:${net_total}")



   change_total = 0
   for i in range(len(profit_col) - 1):
      change = int(profit_col[i + 1]) - int(profit_col[i])
      change_col.append(change)
   
      change_total = change_total + change
 
      avg_change = change_total / (len(profit_col) - 1)

   
   print(f"Average Change:${round(avg_change,2)}")
   
   max_change = max(change_col)
   print(f"Greatest Increase in Profits:${max_change}")
   min_change = min(change_col)
   print(f"Greatest Decrease in Profits:${min_change}")

