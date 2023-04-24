import csv

rows = []

with open("/content/PRO_1-1_C133_StarsDatasetCSVs/star_with_gravity.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)
rows = rows[1:];
data = [];
#Id,Star_name,Distance,Mass,Radius,Gravity
for i in range(len(rows)):
  data.append({"Id":rows[i][0], "Star_Name":rows[i][1], "Distance":rows[i][2], "Mass":rows[i][3], "Radius":rows[i][4], "Gravity":rows[i][5]});