import csv


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
    



#print results
print("ELection Results")
print("----------------------")
print(f"Total Votes: {total_votes!T}")
print("----------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentage[count]}% ({vote_counts[count]})")
print("----------------------")
print(f"Winner: {winner}")
print("----------------------")








# The total number of votes each candidate won
# The winner of the election based on popular vote.