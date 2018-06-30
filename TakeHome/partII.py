#SebastianGonzalez
import sys
from partI import readFile, writeToFile, calculateAverage, calculateSum, findTheLargest, findTheSmallest, countTotalTimes, findStdDev, printOptions, generateRandom
def main():
    option = sys.argv[1]
    times = 0
    if option == "-r":
        fileName = sys.argv[2]
        total = int(sys.argv[3])
        start =int(sys.argv[4])
        end = int(sys.argv[5])
        generateRandom(fileName,total,start,end)
        exit(1)
    while True:
        if times == 5:
            print("Make sure you read the documentation before using the script")
            printOptions()
            exit(1)
        elif option == "-a" or option == "-i":
            if option == "-a":
                file_to_read = sys.argv[2]
                file_to_write = sys.argv[3]
                target_to_find = int(sys.argv[4])
            elif option == "-i":
                file_to_read = input("Enter the input file name: ")
                file_to_write = input("Enter the output file name: ")
                target_to_find = input("Enter the target to be found: ")

            list_after_reading = readFile(file_to_read)
            count = countTotalTimes(target_to_find,list_after_reading)
            list_after_reading = list(map(int,list_after_reading))
            #calling partI functions
            sum = calculateSum(list_after_reading)
            avg = calculateAverage(list_after_reading)
            largest = findTheLargest(list_after_reading)
            smallest = findTheSmallest(list_after_reading)
            stdDev = findStdDev(list_after_reading)

            sum_message = "The sum is: ",sum
            avg_message = "The avg is: ",avg
            largest_message = "The largest item is: ",largest
            smallest_message = "The smallest item is: ",smallest
            count_message = "Ocurrences: ",count
            stdDev_message = "The standard deviation is: ",stdDev
            all_msg = sum_message + avg_message + largest_message + smallest_message + count_message + stdDev_message

            writeToFile(file_to_write,all_msg)
            break
        else:
            times+=1

if __name__ == "__main__":
    main()
