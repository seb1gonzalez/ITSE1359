#Sebastian Gonzalez
import os.path
import math
from random import randint
def printOptions():
    a =""">python3 partII.py [-option] [arguments]
    [-a]: read from argument
        [argument 1]: name of file desired to read
        [argument 2]: name of file desired to write
        [argument 3]: target desired to find on argument 1
    [-i]: interact with user (no arguments needed)
    [-r]: generate random file
        [argument1] corresponds of filename
        [argument2] corresponds to how many numbers to generate
        [argument3] corresponds to start numbers
        [argument4] corresponds to end number"""
    print (a)

def readFile(filename):
    if validateFile(filename):
        with open(filename) as file:
            lines = file.read().splitlines()
        file.close()
        return lines
    else:
        print ("no such file")

def writeToFile(str,list):
    if validateFile(str):
        file = open(str,'w+')
        for items in list:
            file.write("%s \n" % items)
        file.close()
        exit(1)
    else:
        print ("no such file found")

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
    return mylist.count(target)

def findStdDev(mylist):
    avg = calculateAverage(mylist)
    sum = calculateSum(mylist)
    sma = sum - avg #sma stands for sum minus average
    sma_squared = sma**2
    stdev = math.sqrt(sma_squared/ len(mylist))
    return stdev

def generateRandom(filename,total,start,end):
    randomList = []
    i = 0
    while i < total:
        randomList.insert(i,randint(start,end))
        i+=1
    
    if validateFile(filename):
        writeToFile(filename,randomList)
    else:
        print ("no file")
        exit(1)


def main():
    printOptions()
if __name__ == "__main__":
    main()
