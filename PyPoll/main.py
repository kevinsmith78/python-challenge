import csv
#Variables needed for calculation
votes = 0
li_t = 0
khan_t = 0
correy_t = 0
otooley_t = 0
winner_count = 0
#Generate a list of the candidates
can_list = ["li", "kahn", "correy", "otooley"]
#Set input and outfile
file_path = "./Resources/election_data.csv"
out_file = "./Analysis/output.txt"

with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)
#print(f"CSV Header: {csv_header}")
# Read each row of data after the header
    for row in csvreader:
        votes = votes + 1 
#Calculate votes for Li
        if (row[2]) == 'Li':
            li_t = li_t + 1
#Calculate votes for Kahn    
        if (row[2]) == 'Khan':
            khan_t = khan_t + 1
#Calculate votes for Correy       
        if (row[2]) == 'Correy':
            correy_t = correy_t + 1
#Calculate votes for otooley
        if (row[2]) == "O'Tooley":
            otooley_t = otooley_t + 1
    li_pct = round(li_t)/votes * 100,2)
    


    

    
#print results
print("Election Results")
print("----------------------")
print(f"Total Votes: {votes}")
print("----------------------")
print(f"Li: {li_t}")
print(f"Khan: {khan_t}")
print(f"Correy: {correy_t}")
print(f"O'tooley: {otooley_t}")

print("----------------------")

print("----------------------")








# The total number of votes each candidate won
# The winner of the election based on popular vote.