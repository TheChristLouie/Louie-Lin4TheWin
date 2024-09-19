#Christopher Louie
#Death Row Coders
#SoftDev
#File Reading
#2024/9/18
#Time Spent:

import random
occupationsList = []
with open("occupations.csv","r") as file:
    f = file.read().split("\n")
    for item in f:
        item.split(',')
        print(item + "\n")
        print(occupationsList)
        if (item[0] != "Total"):
            occupationsList.append({item[0],item[1]})
    
def randomOccupation():
    percentagesum = 0;
    for job in occupationsList:
        percentagesum += job[0]
    if (percentagesum == 0):
        return null
    x = random.randint(0,percentagesum)
    for job in occupationsList:
        x -= job[0]
        if x <= 0:
            return job[1]
    return null

print(randomOccupation)