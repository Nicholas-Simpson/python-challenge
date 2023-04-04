import os
import csv

##the path may need to be changed depending on where you have the data sheet stored BE AWARE
election_csv = os.path.join("Resources", "election_data.csv")

#define variables we will use for calculations and data storage
total_votes = 0
poll_data = {"candidates": {"name":[],"vote_count":0}}

with open(election_csv,encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        if row[2] not in poll_data["candidates"]["name"]:
            poll_data["candidates"]["name"].append(row[2])

        if row[2] == poll_data["candidates"]["name"]:
            poll_data["candidates"]["vote_count"] += 1

winner = 0

print(poll_data)

# print(f"Election Results\n"
#       f"------------------------------\n"
#       f"Total Votes: {total_votes}\n"
#       f"------------------------------\n"
#       f"{poll_data['candidates']['name']}: {poll_data['candidates']['vote_count']}% ({poll_data['candidates']['vote_count']})\n"
#       f"------------------------------\n"
#       f"Winner: {winner}\n"
#       f"------------------------------\n")

# analysis_txt = os.path.join("analysis", "election_analysis.txt")
# with open(analysis_txt,"w") as txtfile:
#     txtfile.write(f"Election Results\n"
#       f"------------------------------\n"
#       f"Total Votes: {total_votes}\n"
#       f"------------------------------\n"
#       f"{poll_data['candidates']}: {poll_data['vote_count']}% ({poll_data['vote_count']})\n"
#       f"------------------------------\n"
#       f"Winner: {poll_data['winner']}\n"
#       f"------------------------------\n")