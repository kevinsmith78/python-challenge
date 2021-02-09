import csv
#Define Variables
votes = []
count = []
candidates = []
khan = []
correy = []
li = []
otooley = []

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
    # append the data rows together
    votes.append(int(row[0]))
    county.append(row[1])
    candidates.append(row[2])
#Total number of votes
total_votes = (len(votes))
    for candidate in candidates
    if candidate == "Khan":
        khan.append(candidates)
        khan_votes = len(khan)
    elif candidate == "Correy":
        correy.append



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