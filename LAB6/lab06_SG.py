import re

#-------------------For Problem 1---------------------
# if re.search(r'([\d\w][#$%^&*\-\_\!])+',password):
#     if len(password) > 5 and len(password)< 8:
#         print ("Success! but not long enough")
#     elif len(password) > 7:
#         print ("Success! password is long enough")
#     else:
#         print ("Not a long enough password")
# else:
#     print ("Self-destroying")
#-------------------For Problem 2,3,4---------------------
def strongPasswordChecker():
    i = False
    counter = 0
    while (i == False):
        if (counter == 5):
            print ("Too many incorrect attemps, please contact administrator")
            exit(1)
        password = input("Please enter a password\n")
        if (re.search("[a-z]",password) and re.search("[A-Z]",password) and re.search("[0-9]",password)and re.search("[#$%^&*\-\_\!]",password)):
            if len(password) > 7:
                print ("Success! Your password is strong enough")
                print ("Congratulations, you have proven that you are NOT an internet Bot!")
                i = True
            else:
                print ("YOUR PASSWORD IS NOT LONG ENOUGH\n Enter a password of at least 8 characters")
        else:
            print ("Not a valid password")
        counter+=1


def main():
    strongPasswordChecker()


if ("__main__"):
    main()
