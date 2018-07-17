import re
password = input("Please enter a password\n")
#-------------------For Problem 1---------------------
# if re.search(r'([\d\w][#$%^&*\-\_\!])+',password):
#     if len(password) > 5:
#         print ("Success!")
# else:
#     print ("Self-destroying")
#-------------------For Problem 2---------------------
if (re.search("[a-zA-Z]",password) and re.search("[0-9]",password)and re.search("[#$%^&*\-\_\!]",password)):
    if len(password) > 7:
        print ("Success! Your password is strong enough")
    else:
        print ("YOUR PASSWORD IS NOT LONG ENOUGH\n Enter a password of at least 8 characters")
else:
    print ("Not a valid password")
