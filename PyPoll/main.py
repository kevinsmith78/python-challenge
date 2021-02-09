import csv
#Define Variables
total_count_votes = []
number_votes = 0
candidates = [] 
file_path = "./Resources/election_data.csv"
out_file = "./Analysis/output.txt"

with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
# Read each row of data after the header
for row in csvreader:
    # The total number of votes cast (loop)
    total_count_votes = total_count_votes + 1
    candidate = row[2]
# A complete list of candidates who received votes
    if candidate in candidates:
        candidate_index = candidates.index(candidate)
        total_count_votes[candidate_index] = total_count_votes[candidate_index] + 1
        else:
            candidates.append(candidate)
            



# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.