#Sebastian Gonzalez

import os.path
import re


def findCorrectRegex(file):
    goodpattern = re.compile("\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
    list_of_bad = []
    for lines in file:
        badMatches = not re.findall(goodpattern, lines)
        if badMatches:
            list_of_bad.append(lines)
    writeToFile("incorrect.txt",list_of_bad)

def modifyBadPattern(file):
    pattern = re.compile("\d")
    list_of_reformatted = []
    for lines in file:
        matches = re.findall(pattern, lines)
        if matches:
            #(AAA)xxx-xxxx
            matches.insert(0,"(")
            matches.insert(4,")")
            matches.insert(8,"-")
            matches.insert(12,"\n")
            for x in range(0,13):
                list_of_reformatted.append(matches[x])
            rewriteToFile("addressBookFormatted.txt",list_of_reformatted)
def readFile(filename):

    if validateFile(filename):
        with open(filename) as file:
            lines = file.read().splitlines()
        file.close()
        return lines
    else:
        print ("no such file")

def writeToFile(str,list):
    file = open(str,'w+')
    for items in list:
        file.write(items+"\n")
        #file.write("%s \n" % items)
    file.close()
def rewriteToFile(str,list):
    file = open(str,'w+')
    for items in list:
        file.write(items)
        #file.write("%s \n" % items)
    file.close()

def validateFile(filename):
    return os.path.isfile(filename)
def modifyBadPatternfromUSER(number):
    pattern = re.compile("\d")
    list_of_reformatted = []
    matches = re.findall(pattern, number)
    if matches:
        #(AAA)xxx-xxxx
        matches.insert(0,"(")
        matches.insert(4,")")
        matches.insert(8,"-")
        for x in range(0,13):
            list_of_reformatted.append(matches[x])
    return list_of_reformatted
def userInterface():
    phoneNumber = input("Hello, please enter a valid phone number please\n")
    goodpattern = re.compile("\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
    number = []
    matches = re.findall(goodpattern,phoneNumber)
    if matches:
        print("Congratulations your number", phoneNumber, " is in correct order ")
    else:
        goodNumber = modifyBadPatternfromUSER(phoneNumber)
        for x in goodNumber:
            number.append(x)
        print("Your number is incorrect, however here is the correct format: ")
        for x in number:
            print(x, end=" ")

def main():

    #file = readFile("addressbook.txt")
    #findCorrectRegex(file)
    #file_to_change = readFile("incorrect.txt")
    #modifyBadPattern(file_to_change)
    userInterface()


if __name__ == "__main__":
    main()