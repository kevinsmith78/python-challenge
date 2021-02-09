import csv
#Variables needed for calculation
votes = 0
Li = 0
Khan = 0
Correy = 0
Otooley = 0
winner_count = 0
#Generate a list of the candidates
can_list = ["Li", "Kahn", "Correy", "ottoley"]
#Set input and outfile
file_path = "./Resources/election_data.csv"
#out_file = "./Analysis/output.txt"

with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
# Read each row of data after the header
for row in csvreader:
    votes = votes + 1 
# Calculate votes for Li
    if (row[2]) == 'Li'
    Li = Li + 1
    if (row[2]) == 'Khan'
    Khan = Khan + 1
    if (row[2]) == 'Correy'
    Correy = Correy + 1
    if row[2] == 'otooley'
    Otooley = Otooley + 1

    

    
#print results
print("Election Results")
print("----------------------")
print(f"Total Votes: {votes}")
print("----------------------")
print(f"Li: {Li}")
print(f"Khan: {Khan}")
print(f"Correy: {Correy}")
print(f"Otooley" {Otooley})

print("----------------------")

print("----------------------")








# The total number of votes each candidate won
# The winner of the election based on popular vote.