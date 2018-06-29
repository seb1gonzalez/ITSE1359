#SebastianGonzalez
import sys
import partI
def main():
    option = sys.argv[1]
    if option == "-a"
        file_to_read = sys.argv[2]
        file_to_write = sys.argv[3]
        target_to_find = sys.argv[4]
        list_after_reading = readFile(file_to_read)

        #calling partI functions

        sum = calculateSum(list_after_reading)
        avg = calculateAverage(list_after_reading)
        largest = findTheLargest(list_after_reading)
        smallest = findTheSmallest(list_after_reading)
        count = countTotalTimes(target_to_find,list_after_reading)
        stdDev = findStdDev(list_after_reading)

        sum_message = "The sum is: ",sum
        avg_message = "The avg is: ",avg
        largest_message = "The largest item is: ",largest
        smallest_message = "The smallest item is: ",smallest
        count_message = "The algorithm found "+target_to_find+"this times: ",count
        stdDev_message = "The standard deviation is: ",stdDev

        writeToFile(sum_message,file_to_write)
        writeToFile(avg_message,file_to_write)
        writeToFile(largest_message,file_to_write)
        writeToFile(smallest_message,file_to_write)
        writeToFile(count_message,file_to_write)
        writeToFile(stdDev_message,file_to_write)

    elif option == "-i"


if __name__ == "__main__":
    main()
