import csv
file_path ="C:\Users\kevin\Desktop\KS-Homework\python-challenge\03-Python_Hwk\Instructions\PyBank\Resources\budget_data.csv"
with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    print(f" csvHeader:{csv_header}")
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)
    
    # Create Variables
    line_num = 0
    profitloss=[]
    profitlossdates=[]
    profitlosssum=0
    maximum_pl = 0
    minimum_pl = 0
    sum=0

    for row in csvreader
    line_num +=1
    profitloss.append(int(row[1]))
    profitlosssum +- int(row[1])
    profitlossdates.append(row[0])




