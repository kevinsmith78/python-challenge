import csv
file_csv ="C:\Users\kevin\Desktop\KS-Homework\python-challenge\03-Python_Hwk\Instructions\PyBank\Resources\budget_data.csv"
with open(file_csv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    print(f" csvHeader:{csv_header}")
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)
    
    # Create Variables
    total_months_1
    pre_revenue=0
    month_chg=[]
    rev_chg = []
    great_inc = ["",0]
    great_dec = ["",0]
    trevenue = 0







