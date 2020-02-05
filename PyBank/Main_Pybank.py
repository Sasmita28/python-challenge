# First we'll import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join("output", "PyBank.txt")
# Reading using CSV module

with open(csvpath, newline='') as csvfile:

   csvreader = csv.reader(csvfile, delimiter=',')

   csv_header = next(csvreader)

   num_month = 0
   net_total = 0

   profit_col = []
 
   
   for row in csvreader:
      
      num_month += 1
      net_total = net_total + int(row[1])
      profit_col.append(row[1])
      
# casting the profit/losses column as integers
      profit_col = [int(i) for i in profit_col]



   #finding the dates for max profit and  max loss  
      if (max(profit_col) == int(row[1])):
         date_max = row[0]
      elif (min(profit_col) == int(row[1])):
         date_min = row[0]

   change_total = 0
#finding the change 
   for i in range(len(profit_col) - 1):

      
      change = profit_col[i + 1] - profit_col[i]

      if  profit_col[i + 1] == max(profit_col):
         change_max = change
      elif profit_col[i + 1] == min(profit_col):
         change_min = change
   
      change_total = change_total + change
 
      avg_change = change_total / (len(profit_col) - 1)

   print(f"Total Months: {num_month}")
   print(f"Total: ${net_total}")
   print(f"Average Change: ${round(avg_change,2)}")
   print(f"Greatest Increase in Profits:{date_max} (${change_max})")
   print(f"Greatest Decrease in Profits:{date_min} (${change_min})")
 
 

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as writer:

    # Writing the lines to the text file 
    writer.writelines(f"Total Months: {num_month}\n")

    writer.writelines(f"Total: ${net_total}\n")

    writer.writelines(f"Average Change: ${round(avg_change,2)}\n")

    writer.writelines(f"Greatest Increase in Profits:{date_max} (${change_max})\n")

    writer.writelines(f"Greatest Decrease in Profits:{date_min} (${change_min})")
