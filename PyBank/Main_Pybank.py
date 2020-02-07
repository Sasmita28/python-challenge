# First we'll import the os module
import os

# Module for reading CSV files
import csv


# giving path for the input as well as output files
csvpath = os.path.join('Resources', 'budget_data.csv')

output_path = os.path.join("output", "PyBank.txt")

# Reading using CSV module
with open(csvpath, newline='') as csvfile:

   csvreader = csv.reader(csvfile, delimiter=',')

   csv_header = next(csvreader)

   # intializing the variables
   num_month = 0
   net_total = 0
   profit_col = []
 
   # Calculating no. of months and net total by looping through csvreader
   for row in csvreader:
      
      num_month += 1
      net_total = net_total + int(row[1])

      #appending profit/loss column values to profit_col
      profit_col.append(row[1])
      
      #casting the profit/losses column as integers
      profit_col = [int(i) for i in profit_col]



   #finding the dates for max profit and  max loss  
      if (max(profit_col) == int(row[1])):
         date_max = row[0]
      elif (min(profit_col) == int(row[1])):
         date_min = row[0]

   #intializng change total
   change_total = 0
   #finding the change 
   for i in range(len(profit_col) - 1):

      change = profit_col[i + 1] - profit_col[i]

      # Finding the max chage  and min change using max  and min profit
      if  profit_col[i + 1] == max(profit_col):
         change_max = change
      elif profit_col[i + 1] == min(profit_col):
         change_min = change


      # calculating the total chage
      change_total = change_total + change
      #calculating the average change
      avg_change = change_total / (len(profit_col) - 1)


   #Printing the results to the terminal
   print(f"Total Months: {num_month}")
   print(f"Total: ${net_total}")
   print(f"Average Change: ${round(avg_change,2)}")
   print(f"Greatest Increase in Profits:{date_max} (${change_max})")
   print(f"Greatest Decrease in Profits:{date_min} (${change_min})")
 
 

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as writer:

   # Writing the lines to the PyBank.text file 
    writer.writelines(f"Total Months: {num_month}\n")

    writer.writelines(f"Total: ${net_total}\n")

    writer.writelines(f"Average Change: ${round(avg_change,2)}\n")

    writer.writelines(f"Greatest Increase in Profits:{date_max} (${change_max})\n")

    writer.writelines(f"Greatest Decrease in Profits:{date_min} (${change_min})")
