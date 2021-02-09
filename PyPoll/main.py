import csv
#Define Variables
total_count_votes = []
number_votes = 0
candidates = [] 
percentage = []
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
        total_count_votes = total_count_votes[candidate_index] + 1
    else:
        candidates.append(candidate)
        total_count_votes.append(1)
# The percentage of votes each candidate won
percentages = []
m_votes = total_count_votes[0]
m_out = 0
for count in range(len(candidates)):
    vote_percentage = total_count_votes[count]/number_votes*100
    percentages.append(vote_percentage)
    if total_count_votes[count] > m_votes:
        m_votes = total_count_votes[count]
        print(m_votes)
        m_out = count
winner = candidates[m_out]
#print results
print("ELection Results")
print("----------------------")
print(f"Total Votes: {total_count_votes}")
print("----------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentage[count]}% ({vote_counts[count]})")
print("----------------------")
print(f"Winner: {winner}")
print("----------------------")








# The total number of votes each candidate won
# The winner of the election based on popular vote.