import os
import csv

##the path may need to be changed depending on where you have the data sheet stored BE AWARE
election_csv = os.path.join("Resources", "election_data.csv")

#define variables we will use for calculations and data storage
total_votes = 0
candidates = {}


with open(election_csv,encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1 
        else: candidates[row[2]] = 1
         
winner_count = 0

for candidate in candidates.keys():
    if candidates[candidate] > winner_count:
        winner_count = candidates[candidate]
        winner = candidate



print(f"Election Results\n"
      f"------------------------------\n"
      f"Total Votes: {total_votes}\n"
      f"------------------------------\n")

for candidate in candidates:
      print(f"{candidate}: {candidates[candidate]/total_votes:.3%} ({candidates[candidate]})")
      
print(f"------------------------------\n"
      f"Winner: {winner}\n"
      f"------------------------------\n")

analysis_txt = os.path.join("analysis", "election_analysis.txt")
with open(analysis_txt,"w") as txtfile:
    txtfile.write(f"Election Results\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes}\n")
    
    for candidate in candidates:
        txtfile.write(f"{candidate}: {candidates[candidate]/total_votes:.3%} ({candidates[candidate]})\n")
      
    txtfile.write(f"------------------------------\n"
        f"Winner: {winner}\n"
        f"------------------------------")