import csv
with open('D:\\OUTSIDE_STUFF\\PANDAS\\week_1.csv','r') as csvfile:
    rows=csv.reader(csvfile)
    for row in rows:
        print(row)