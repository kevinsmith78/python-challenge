import csv
votes = 0
vote count = 0
vote_percent = []
candidates = []
diff_candidates = []
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
        votes = votes + 1
        candidate.append(row[2])
        
    
#print results
print("Election Results")
print("----------------------")
print("Total Votes:")
print("----------------------")

print("----------------------")

print("----------------------")








# The total number of votes each candidate won
# The winner of the election based on popular vote.