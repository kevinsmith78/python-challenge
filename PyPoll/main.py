import csv
#The total number of  votes casr
Votes = []
County = []
Candidates =[]
khan = []
correy = []
greatest_votes = ["",0}]
C_options = []
candidate_v = {}

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
        votes = votes + 1
        t_candidates = row["Candidate"]

        if row[]

# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.