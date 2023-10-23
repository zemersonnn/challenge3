# read the csv file
import os
import csv 

total_votes_cast = []
total = []
canidates = []
votes = []

csvpath = os.path.join("..","PyPoll","Resources","election_data.csv")
with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader: 
        # total number of votes cast 
        if row[2] not in canidates:
            canidates.append(row[2])
            canidates_list = canidates.index(row[2])
            total_votes_cast.append(1)
        else: 
            canidates_list = canidates.index(row[2])
            total_votes_cast.append(1)
            total_votes_cast[canidates_list] += 1
        
        total = len(total_votes_cast)
        # a complete list of candidates who received votes 
        # the percentage of votes each canidate won
        # the total number of votes each canidate won
        for j in range(len(canidates)):
            percent = (total_votes_cast[j]/total)*100
            percent_var = (f'{str(round(percent, 3))}%')
            votes.append(percent_var)

        # the winner of the election based popular vote
        winner = max(total_votes_cast)
        winner_list = total_votes_cast.index(winner)
        best_canidate = canidates[winner_list]

    # print
    print(f'Total number of votes cast = {total}')
    for i in range(len(canidates)):
        print(f'{str(canidates[i])}: {str(votes[i])} ({str(total_votes_cast[i])})')
    print(f'Winner: {best_canidate}')

    # export text file with results
    export_file = "election_data_analysis.txt"

    # format
    file = open(export_file, 'w')
    file.write("Election Results\n")
    file.write("-----------------------------\n")
    file.write(f'Total Votes: {total}\n')
    file.write("-----------------------------\n")
    for i in range(len(canidates)):
        file.write(f'{str(canidates[i])}: {str(votes[i])} ({str(total_votes_cast[i])})\n')
    file.write("-----------------------------\n")
    file.write(f'Winner: {best_canidate} \n')
    file.write("-----------------------------\n")
    file.close()