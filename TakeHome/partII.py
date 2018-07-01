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


def _r_random_selected(filename,total,start,end):

    generateRandom(filename,total,start,end)
    sys.exit(1)


def main():
    attemps = 0
    attemp_limit = 5
    option = sys.argv[1]
    while attemps < attemp_limit:
        print ("Remaining attemps = ", attemp_limit - attemps)
        confirm_option = input("Please retype option to confirm script, current option is: "+option)
        if confirm_option == "-i" or confirm_option == "-r" or confirm_option == "-a":
            option = confirm_option
            if option == "-r":
                if len(sys.argv) < 5:
                    print ("missing arguments")
                    attemps+=1

                    try:
                        file = input("What is the name of the input file?\n")
                        total = int(input("How many random numbers?\n"))
                        begin = int(input("start number: "))
                        end = int(input("end number:"))
                    except ValueError:
                        attemps+=1

                        continue
                    _r_random_selected(file,total,begin,end)
                    sys.exit(1)


                else:
                    filename = sys.argv[2]
                    total = int(sys.argv[3])
                    start =int(sys.argv[4])
                    end = int(sys.argv[5])
                    _r_random_selected(filename,total,start,end)
                    sys.exit(1)

            elif option == "-a":
                if len(sys.argv) < 4:
                    print ("mising arguments")
                    attemps+=1

                    try:
                        file_to_read = input("Enter the input file name: ")
                        file_to_write = input("Enter the output file name: ")
                        target_to_find = int(input("Enter the target to be found: "))
                    except ValueError:
                        attemps+=1

                        continue
                    make_operations(file_to_read,file_to_write,target_to_find)
                    sys.exit(1)
                else:
                    file_to_read = sys.argv[2]
                    file_to_write = sys.argv[3]
                    target_to_find = int(sys.argv[4])
                    make_operations(file_to_read,file_to_write,target_to_find)
                    sys.exit(1)

            elif option == "-i":
                try:
                    file_to_read = input("Enter the input file name: ")
                    file_to_write = input("Enter the output file name: ")
                    target_to_find = int(input("Enter the target to be found: "))
                except ValueError:
                    attemps+=1

                    continue
                make_operations(file_to_read,file_to_write,target_to_find)
                sys.exit(1)
        else:
            attemps+=1



if __name__ == "__main__":
    main()
