import os
import csv

##the path may need to be changed depending on where you have the data sheet stored BE AWARE
budget_csv = os.path.join("Resources", "budget_data.csv")

#define variables we will use for calculations and data storage
totalPL = 0
total_months = 0
prvchange = 0
total_change = 0
Greatest = {
    "Increase": 0,
    "inMonth" : "",
    "Decrease": 0,
    "deMonth" : ""}


with open(budget_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    first_row = next(csvreader)
    totalPL = int(first_row[1]) + totalPL
    total_months = total_months + 1
    prvchange = int(first_row[1])

    for row in csvreader:
        total_months += 1
        current = int(row[1])
        totalPL = current + totalPL
        total_change += (current - prvchange)

        if ((current - prvchange) > Greatest["Increase"]):
            Greatest["Increase"] = (current - prvchange)
            Greatest["inMonth"] = row[0]
        
        if ((current - prvchange) < Greatest["Decrease"]):
            Greatest["Decrease"] = (current - prvchange)
            Greatest["deMonth"] = row[0]
            
        

        prvchange = current

    avgChange = round(total_change / (total_months - 1), 2)



print("Finacial Analysis")
print("-----------------------------")
print(f"Total months: {total_months}")
print(f"Total: ${totalPL}")
print(f"Average Change: ${avgChange}")
print(f"Greatest Increase in Profits: {Greatest['inMonth']} (${Greatest['Increase']})")
print(f"Greatest Decrease in Profits: {Greatest['deMonth']} (${Greatest['Decrease']})")


analysis_txt = os.path.join("analysis", "profit_loss_analysis.txt")
with open(analysis_txt,"w") as txtfile:
    txtfile.write("Finacial Analysis\n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"Total months: {total_months}\n")
    txtfile.write(f"Total: ${totalPL}\n")
    txtfile.write(f"Average Change: ${avgChange}\n")
    txtfile.write(f"Greatest Increase in Profits: {Greatest['inMonth']} (${Greatest['Increase']})\n")
    txtfile.write(f"Greatest Decrease in Profits: {Greatest['deMonth']} (${Greatest['Decrease']})")