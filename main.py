import os
import csv


PyPollcsv = os.path.join("C:\Users\ryanw\python-challenge\PyPoll","Resources","election_data.csv")


count = 0
candidatelist = []
candidate = []
vote_c = []
vote_p = []


with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        count = count + 1
        
        candidatelist.append(row[2])
        
    for x in set(candidatelist):
        candidate.append(x)
       
        y = candidatelist.count(x)
        vote_c.append(y)
       
        z = (y/count)*100
        vote_p.append(z)
        
    winningvote = max(vote_c)
    winner = candidate[vote_c.index(winningvote)]
    

 
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(candidate)):
            print(candidate[i] + ": " + str(vote_p[i]) +"% (" + str(vote_c[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")


with open('election.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(candidate))):
        text.write(candidate[i] + ": " + str(vote_p[i]) +"% (" + str(vote_c[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")