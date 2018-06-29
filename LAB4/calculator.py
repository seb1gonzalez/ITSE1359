import operator
import math
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print ("Hello Mr. Robot, please enter an operator first\n [+,-,/,*,!,sqrt,log]\nThen enter a number when prompted.\n")
oper = input("Operator: ")
try:
    num1 = int(input("Enter first number: "))
except ValueError:
    print ("That was not a number")
    exit(1)
if oper == "sqrt":
    print ("Sqrt: ",math.sqrt(num1))
elif oper == "!":
    print ("Factorial: "+str(factorial(num1)))
elif oper == "log":
    print ("Log: ", math.log10(num1))

else:
    try:
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print ("That was not a number")
        exit(1)
    if oper =="+":
        print ("Sum: "+str(num1 + num2))
    if oper =="-":
        print ("Sub: "+str(num1 - num2))
    if oper =="/":
        if num2 == 0:
            print ("Can't divide by zero")
        else:
            print ("Div: " + str(num1/num2))
    if oper =="*":
        print("Mult: "+ str(num1*num2))
    else:
        print ("operator not found")
    exit(1)
