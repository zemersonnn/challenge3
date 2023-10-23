
# read the csv file
import os
import csv 

profits_losses = []
row_count = 0
total = 0 
month = []
change = []

csvpath = os.path.join("..","PyBank","Resources","budget_data.csv")
with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) 
    
    for row in csvreader: 
        # total number of months included in the dataset
        row_count += 1
       
    # net total amount of "Profits/Losses" over the entire period 
        total += int(row[1])
       
    # the changes in "profits/losses" and then the avg of those changes
        month.append(row[0])
        profits_losses.append(int(row[1]))
        change.append(profits_losses[row_count-1] - profits_losses[row_count-2])

    total_change = sum(change)
    average_change = round(total_change/(len(change)-1), 2)

    # greatest increase in proftis (date and amount) 
    increase_profit = max(change)
    greatest_increase = change.index(increase_profit)

    # greatest decrease in profits (date and amount)
    decrease_profit = min(change)
    greatest_decrease = change.index(decrease_profit)

    print(f'{row_count} months')
    print(f'net total amt of profits and losses = {total}')
    print(f'The changes in profits/losses then the average of those changes = {average_change}')
    print(f'The greatest increase = {month[greatest_increase]} ${increase_profit}')
    print(f'The greatest decrease = {month[greatest_decrease]} ${decrease_profit}')

    # export text file with results
    export_file = "budget_data_analysis.txt"
    
    # format
    file = open(export_file, 'w')
    file.write("Financial Analysis\n")
    file.write("-----------------------------\n")
    file.write(f'{row_count} months\n')
    file.write(f'net total amt of profits and losses = {total}\n')
    file.write(f'The changes in profits/losses then the average of those changes = {average_change}\n')
    file.write(f'The greatest increase = {month[greatest_increase]} ${increase_profit}\n')
    file.write(f'The greatest decrease = {month[greatest_decrease]} ${decrease_profit}\n')
    file.close()



