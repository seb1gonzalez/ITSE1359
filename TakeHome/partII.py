#SebastianGonzalez
import sys
from partI import readFile, writeToFile, calculateAverage, calculateSum, findTheLargest, findTheSmallest, countTotalTimes, findStdDev, printOptions, generateRandom

def make_operations(file_to_read,file_to_write,target_to_find):

    list_after_reading = readFile(file_to_read)
    list_after_reading = list(map(int,list_after_reading)) #transforms str to int

    #calling partI functions
    count = countTotalTimes(target_to_find,list_after_reading)
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

    # see results.txt to see output
    writeToFile(file_to_write,all_msg)


def _r_random_selected():
    filename = sys.argv[2]
    total = int(sys.argv[3])
    start =int(sys.argv[4])
    end = int(sys.argv[5])
    generateRandom(filename,total,start,end)
    sys.exit(1)


def main():
    attemps = 0
    attemp_limit = 5
    while attemps < attemp_limit:
        

        option = sys.argv[1]
        if option == "-r":
            if len(sys.argv) < 5:
                print ("missing arguments")

            else:
                _r_random_selected()

        elif option == "-a":
            if len(sys.argv) < 4:
                print ("mising arguments")
                file_to_read = sys.argv[2]
                file_to_write = sys.argv[3]
                target_to_find = int(sys.argv[4])
                make_operations(file_to_read,file_to_write,target_to_find)

        elif option == "-i":
            file_to_read = input("Enter the input file name: ")
            file_to_write = input("Enter the output file name: ")
            target_to_find = int(input("Enter the target to be found: "))
            make_operations(file_to_read,file_to_write,target_to_find)

if __name__ == "__main__":
    main()
