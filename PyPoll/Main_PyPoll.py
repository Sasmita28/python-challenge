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
    
    #intializing the variables
    vote_id = []
    candidate =[]
    candidate_unq = []
    candidate_info = {}
    
   
   # Calculating no. of votes by looping through csvreader
    for row in csvreader:
        vote_id.append(row[0])
        candidate.append(row[2])
        #Find the total number of votes
        total_votes = len(vote_id)

    #finding the unique candidates
    for x in candidate:
        if x not in candidate_unq:
            candidate_unq.append(x)
    #print(candidate_unq)

    #finding the number of win and percentage of win for each candidate
    num1 = candidate.count(candidate_unq[0])
    percent_win1 = f"{round((num1/total_votes) * 100,2)}%"
    num2 = candidate.count(candidate_unq[1])
    percent_win2 = f"{round((num2/total_votes) * 100,2)}%"
    num3 = candidate.count(candidate_unq[2])
    percent_win3 = f"{round((num3/total_votes) * 100,2)}%"
    num4 = candidate.count(candidate_unq[3])
    percent_win4 = f"{round((num4/total_votes) * 100,2)}%"

    #finding the winner from the percent win for each candidate
    if (percent_win1 > percent_win2 and percent_win1 > percent_win3 and percent_win1 > percent_win4):
        winner = candidate_unq[0]
    elif (percent_win2 > percent_win1 and percent_win2 > percent_win3 and percent_win2 > percent_win4):
        winner = candidate_unq[1]
    elif (percent_win3 > percent_win1 and percent_win3 > percent_win2 and percent_win3 > percent_win4):
        winner = candidate_unq[2]
    elif (percent_win4 > percent_win1 and percent_win4 > percent_win2 and percent_win4 > percent_win3):
        winner = candidate_unq[3]

    #writting to a dictionary
    candidate_info[candidate_unq[0]]=[percent_win1,num1]
    candidate_info[candidate_unq[1]]=[percent_win2,num2]
    candidate_info[candidate_unq[2]]=[percent_win3,num3]
    candidate_info[candidate_unq[3]]=[percent_win4,num4]

    #print(candidate_info)

    #printing to the terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes : {total_votes}")
    print("-------------------------")
    print(f"{candidate_unq[0]}:{percent_win1} ({num1})")
    print(f"{candidate_unq[1]}:{percent_win2} ({num2})")
    print(f"{candidate_unq[2]}:{percent_win3} ({num3})")
    print(f"{candidate_unq[3]}:{percent_win4} ({num4})")
    print("-------------------------")
    print(f"Winner:{winner}")
    print("-------------------------")


# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as writer:

   # Writing the lines to the PyPoll.text file 
    writer.writelines("Election Results\n")

    writer.writelines("------------------------\n")

    writer.writelines(f"Total Votes : {total_votes}\n")

    writer.writelines("------------------------\n")

    writer.writelines(f"{candidate_unq[0]}:{percent_win1} ({num1})\n")

    writer.writelines(f"{candidate_unq[1]}:{percent_win2} ({num2})\n")

    writer.writelines(f"{candidate_unq[2]}:{percent_win3} ({num3})\n")

    writer.writelines(f"{candidate_unq[3]}:{percent_win4} ({num4})\n")

    writer.writelines("-------------------------\n")

    writer.writelines(f"Winner:{winner}\n")

    writer.writelines("-------------------------")