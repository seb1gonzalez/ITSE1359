# Sebastian Gonzalez
import sys
def sumEvens(n):
    count = 0
    sum = 0
    while count < n:
        sum += count
        count+=2
    print ("The sum of evens is ",sum)

def sumOdds(n):
    count = 0
    sum = 0
    while count < n:
        odd = 2*count+1
        sum += odd
        count+=1
    print ("The sum of odds is ",sum)

def oddAverage(n):
    count = 0
    sum = 0
    while count < n:
        odd = 2*count+1
        sum += odd
        count+=1
    avg = sum/n
    print ("The average of odds is ",avg)

def calcualteAvg(n):
    count = 0
    sum = 0
    while count < n:
        sum += count
        count+=1
    avg = sum/n
    print ("The average is ", avg)
def fib(n):

    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def addRange(n,m):
    count = n
    sum = 0
    while count <= m:
        sum += count
        count+=1
    print("Addition in range is ",sum)
def generatePrimes(n):# 2 for loops to check if the counter is a prime number until we hit n.
    for i in range(1,n):
        x = 0
        for j in range(1,i+1):
            y= i%j
            if y == 0:
                x+=1
        if x == 2:
            print (str(i))

def main():
    selection = 0
    selection = int(sys.argv[1])
    argument1 = int(sys.argv[2])


    if selection == 1: sumEvens(argument1)
    elif selection == 2:sumOdds(argument1)
    elif selection == 3: oddAverage(argument1)
    elif selection == 4: calcualteAvg(argument1)
    elif selection == 5:
        print ("Fibonacci: ")
        n = argument1
        for i in range(n):
            print (fib(i))
    
    elif selection == 6: print("Factorial: ",factorial(argument1))
    elif selection == 7:
        argument2 = int(sys.argv[3])
        addRange(argument1,argument2)
    elif selection == 8: generatePrimes(argument1)
    else:
        print("not possible")

if __name__ == "__main__":
    main()
