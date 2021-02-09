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
#Calculate Percent Of votes   
    li_pct = round(li_t/votes * 100,2)
    k_pct = round (khan_t/votes * 100,2)
    c_pct = round (correy_t/votes * 100,2)
    o_pct = round (otooley_t/votes * 100,2)
#Create Lists for percentages
    tot_pct = [k_pct,c_pct,li_pct,o_pct]
#zip the vairables (dictionary) together to produce results
    total_pct = dict(zip(can_list,tot_pct))
#find the winner using max function
winner = max(total_pct, key=total_pct.get)
   
#print results
print("Election Results")
print("----------------------")
print(f"Total Votes: {votes}")
print("----------------------")
print(f"Li: {li_pct}% ({li_t})")
print(f"Khan: {k_pct}% ({khan_t})")
print(f"Correy: {c_pct}% ({correy_t})")
print(f"O'tooley: {o_pct}% ({otooley_t})")
print("----------------------")

print("----------------------")








# The total number of votes each candidate won
# The winner of the election based on popular vote.