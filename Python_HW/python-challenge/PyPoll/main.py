import os
import csv

file_name = "Main_PyPoll"

Total_Votes = 0
Candidate = ""
Candidate_Votes = {}
Candidate_Percentages ={}
Winner_Votes = 0
Winner = ""

filepath = os.path.join(".", "Resources", "election_data.csv")
with open(filepath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        Total_Votes = Total_Votes + 1
        Candidate = row[2]
        if Candidate in Candidate_Votes:
            Candidate_Votes[Candidate] = Candidate_Votes[Candidate] + 1
        else:
            Candidate_Votes[Candidate] = 1

for Person, Vote_Count in Candidate_Votes.items():
    Candidate_Percentages[Person] = '{0:.0%}'.format(Vote_Count / Total_Votes)
    if Vote_Count > Winner_Votes:
        Winner_Votes = Vote_Count
        Winner = Person


print("Election Results")

print(f"Total Votes: {Total_Votes}")

for person, Vote_Count in Candidate_Votes.items():
    print(f"{person}: {Candidate_Percentages[person]} ({Vote_Count})")

print(f"Winner: {Winner}")

save_file = file_name.strip(".csv") + ".txt"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as text:

    text.write(f"Total Votes: {Total_Votes}" + "\n")
    for person, Vote_Count in Candidate_Votes.items():
        text.write(f"{person}: {Candidate_Percentages[person]} ({Vote_Count})" + "\n")
    text.write(f"Winner: {Winner}" + "\n")
    text.write(f"BOOM GOES THE DYNAMITE!")