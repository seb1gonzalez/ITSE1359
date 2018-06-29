while True:
    try:
        num = int(input("Give me a number "))
    except ValueError:
        print("Try again huuuman!")
    else:
        file = open("results.txt","w+")
        for i in range(num):
            try:
                x = int(input("Give me another number "))
            except ValueError:
                print("not a number dude!")
                break
            else:
                file.write(str(x)+"\n")
        file.close()
        break
with open('results.txt','r') as input:
    count = 0
    total = 0
    for line in input:
        num = int(line)
        total += num
        count += 1
    input.close()
average = total/count
file = open("results.txt", "w+")
file.write("sum: " + str(total) + "\n" + "average: " + str(average)+"\n")
file.close()
