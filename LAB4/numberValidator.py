try:
    num = int(input("Give me a number "))
except ValueError:
    print("Sorry that is not a number, good bye\n")
    exit(1)

if num == 0:
    print(num)
elif num > 100:
    print("Sorry, the limit accepted is 100, try again.\n")
    exit(1)
else:
    for i in range(num+1):
        print(i)
