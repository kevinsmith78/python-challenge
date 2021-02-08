import csv
#The total number of  votes cast
Votes = []
County = []
Candidates =[]
khan = []
correy = []
li = []
otooley =[]


with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
file_path = "./Resources/election_data.csv"
out_file = "./Analysis/output.txt"

# Read each row of data after the header
for row in csvreader:
    # The total number of votes cast (loop)
    votes.append(int(row[0])
    County.append(row[1])
    Candidates.append(row[2])
    t_votes = (len(Votes))
    print (t_votes)


        #if row[]

# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.