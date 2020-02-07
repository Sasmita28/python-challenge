# First we'll import the os module
import os

# Module for reading CSV files
import csv


# giving path for the input as well as output files
csvpath = os.path.join('Resources', 'election_data.csv')

output_path = os.path.join("output", "PyPoll.txt")

# Reading using CSV module
with open(csvpath, newline='') as csvfile:

   csvreader = csv.reader(csvfile, delimiter=',')

   csv_header = next(csvreader)

   vote_id = []
   candidate =[]
   candidate_unq = []
   candidate_info = {}
   num_win = []
   prev_num = []
   percent_win_candidate = []
   name_to_check = input("What candidate do you want to look for? ")
   num = 0
   
   # Calculating no. of votes and net total by looping through csvreader
   for row in csvreader:

      vote_id.append(row[0])
      candidate.append(row[2])
      #Find the total number of votes
      total_votes = len(vote_id)


      if name_to_check.title() == row[2]:
         
         num += 1
      
         percent_win =round((num / total_votes) * 100,4)

         candidate_info[name_to_check] = num


   for x in candidate:
      if x not in candidate_unq:
         candidate_unq.append(x)
   #print(candidate_info)
   

   

   print(candidate_unq)
   print(candidate_info)
#   print(prev_num)
   print("Election Results")
   print("------------------------")
   print(f"Total Votes: {total_votes}")
   print("------------------------")
   print(f"{name_to_check}: {percent_win}% ({num})")