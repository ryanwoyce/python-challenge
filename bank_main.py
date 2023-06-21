import os
import csv

cvvpath = os.path.join("\Users\\ryanw\python-challenge\PyBank", "Resources", "Budget_data.csv")
profit = []
monthly_changes = []
date = []

 
count = 0
total = 0
total_change = 0
initial_profit = 0


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:    
  
      count = count + 1 


      date.append(row[0])

      
      profit.append(row[1])
      total = total + int(row[1])

      
      profits = int(row[1])
      monthly_change_profits = profits - initial_profit

      #Store these monthly changes in a list
      monthly_changes.append(monthly_change_profits)

      total_change = total_change + monthly_change_profits
      initial_profit = profits

      
      average = (total_change/count)
      
      
      increase = max(monthly_changes)
      decrease = min(monthly_changes)

      increase_date = date[monthly_changes.index(increase)]
      decrease_date = date[monthly_changes.index(decrease)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total))
    print("Average Change: " + "$" + str(int(average)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(increase) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(decrease)+ ")")
    print("----------------------------------------------------------")

with open('fin.analysis.txt', 'w') as text:
    
    text.write("Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("Total Months: " + str(count) + "\n")
    text.write("Total Profits: " + "$" + str(total) +"\n")
    text.write("Average Change: " + '$' + str(int(average)) + "\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(increase) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(decrease) + ")\n")