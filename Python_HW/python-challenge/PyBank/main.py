import os
import csv

file_name = "Main_PyBank"

csvpath = os.path.join("..", "..", "Resources", "budget_data.csv")
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')

    Months = 0
    Profits_Losses = 0

    rows = [r for r in csvreader]

    Change_Profits_Losses = int(rows[1][1])
    max = rows[1]
    min = rows[1]

    for i in range(1,len(rows)):
        
        Months = Months+1
        row = rows[i]
        Profits_Losses = int(row[1]) + Profits_Losses
        
        if i > 1:
            Change_Profits_Losses = Change_Profits_Losses + int(row[1])-int(rows[i-1][1])
        if int(max[1]) < int(row[1]):
            max = row
        if int(min[1]) > int(row[1]):
            min = row

Average= int(Profits_Losses /Months)

print("Total Months:                         " + str(Months))
print("Total Profits:                        " +"$" +str(Profits_Losses))       
print("Average Change in Profits/Losses:     " +"$"+ str(Average))
print("Greatest Increase in Profits:         " + str(max[0])+" ($" + str(max[1])+")")
print("Greatest Decrease in Profits:         " + str(min[0])+" ($" + str(min[1])+")")


save_file = file_name.strip(".csv") + ".txt"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as text:

    text.write("Total Months:                         " + str(Months) + "\n")
    text.write("Total Profits:                        " +"$" +str(Profits_Losses) + "\n")       
    text.write("Average Change in Profits/Losses:     " +"$"+ str(Average) + "\n")
    text.write("Greatest Increase in Profits:         " + str(max[0])+" ($" + str(max[1])+")" + "\n")
    text.write("Greatest Decrease in Profits:         " + str(min[0])+" ($" + str(min[1])+")" + "\n")