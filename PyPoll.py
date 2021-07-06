# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete ,ist of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize total vote counter
total_votes = 0

#initialize candidate list
candidate_options = []
#Declare empty dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader: 
        total_votes += 1

        #creating candidate list
        candidate_name = row[2]

        # Getting the list of candidates and adding the to a dict
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1



# % of votes for each candidate
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) *100

    print(f'{candidate_name}: {vote_percentage:.1f}% {votes:,}')

    #Determine winner and their values
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage

        winning_candidate = candidate_name


winning_candidate_summary = (
    f"-----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n"
    f"-----------------------\n")

print(winning_candidate_summary)



