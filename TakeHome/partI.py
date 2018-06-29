import os.path
import math
from random import randint
def printOptions():
    a =""">python3 partII.py [-option] [arguments]
    [-a]: read from argument
        [argument 1]: name of file desired to read
        [argument 2]: name of file desired to write
        [argument 3]: target desired to fin on argument 1
    [-i]: interact with user (no arguments needed)
    [-r]: generate random file
        [argument1] corresponds of filename
        [argument2] corresponds to how many numbers to generate
        [argument3] corresponds to start numbers
        [argument4] corresponds to end number"""
    print (a)

def readFile(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    file.close()

def writeToFile(str,list):
    file = open(str,'w')
    for items in list:
        file.write("%s \n" % items)
    file.close()

def validateFile(filename):
    return os.path.isfile(filename)

def calculateSum(mylist):
    b = sum(mylist)
    return b

def calculateAverage(mylist):
    x = sum(mylist)
    y = len(mylist)
    avg = x/y
    return avg
def findTheLargest(mylist):
    return max(mylist)

def findTheSmallest(mylist):
    return min(mylist)

def countTotalTimes(target,mylist):
    found = 0
    for i in len(mylist):
        if mylist[i] == target:
            found+=1
    return found

def findStdDev(mylist):
    avg = calculateAverage(mylist)
    sum = calculateSum(mylist)
    sma = sum - avg #sma stands for sum minus average
    sma_squared = sma**2
    stdev = math.sqrt(sma_squared/ len(mylist))
    return stdev
def generateRandom(filename,total,start,end):
    i = 0
    randomList = []
    while i < total:
        randomList[i] = randint(start,end)
    if validateFile(filename):
        writeToFile(filename,randomList)
    else:
        print ("no file")

def main():
    printOptions()
if __name__ == "__main__":
    main()
