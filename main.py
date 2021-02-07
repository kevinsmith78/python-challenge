# import csv
import csv
# file I need to load
file_csv ="C:\Users\kevin\Desktop\KS-Homework\python-challenge\03-Python_Hwk\Instructions\PyBank\Resources\budget_data.csv"
# Variables that I plan to work with
Tomonth = 0
prevrevenue = 0
TOrevenue =0
revenuechg =0
revenue_chg =[]
monthof_chg = []
great_inc = ["",0]
great_dec = ["",0]

# read the appropirate file
with open(file_csv) as csvfile:
    # CSV reader specifies variable that holds contents
    csvreader = csv.reader(csvfile)
    print(f"csvHeader:{csv_header}")
    # Read the header row first (skip it)
    csv_header = next(csvreader)

# Loop through number sequence
for row in reader  
    #totals
    Tomonth = Tomonth +1
    TOrevenue = TOrevenue +int(row["Revenue"]) 

#develop the calculations
    revenuechg=int(row["Revenue"]) - prevrevenue
    prevrevenue = int(row["Revenue"])
    monthof_chg = monthof_chg + [row["Date"]]

    if (revenue_chg>great_inc[1])
        great_inc[1] = revenuechg
        great_inc[0] = revenuechg

        











