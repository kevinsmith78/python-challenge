import csv
#Variables needed for calculation
votes = 0
li_t = 0
khan_t = 0
correy_t = 0
otooley_t = 0
winner_count = ''
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
# Simplify results   
    if li_t > correy_t and li_t > otooley_t and li_t > khan_t:
        winner_count = "Li"
    elif khan_t > correy_t and khan_t > li_t >khan_t > otooley_t:
        winner_count = "Khan"
    elif correy_t > otooley_t and correy_t > khan_t and correy_t > li_t:
        winner_count = "Correy"
    elif otooley_t > correy_t and otooley_t > li_t and otooley_t > khan_t:
        winner_count = "O'Tooley"  
    
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
print(f"Winner: {winner_count}")
print("----------------------")

with open(out_file, 'w') as outputfile:
    outputfile.write("Election Results")
    outputfile.write("----------------------")
    outputfile.write("Total Votes: {votes}")
    outputfile.write("----------------------")
    outputfile.write("Li: {li_pct}% ({li_t})")
    outputfile.write("Khan: {k_pct}% ({khan_t})")
    outputfile.write("Correy: {c_pct}% ({correy_t})")
    outputfile.write("O'tooley: {o_pct}% ({otooley_t})")
    outputfile.write("----------------------")
    outputfile.write("Winner: {winner_count}")
    outputfile.write("----------------------")






# The total number of votes each candidate won
# The winner of the election based on popular vote.