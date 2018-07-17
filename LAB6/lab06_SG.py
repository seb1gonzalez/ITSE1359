import re
password = input("Please enter a password\n")

if re.search(r'([\d\w][#$%^&*\-\_\!])+',password):
    if len(password) > 5:
        print ("Success!")
else:
    print ("Self-destroying")
