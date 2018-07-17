import re
password = input("Please enter a password")
if re.search(r'[A-Za-z0-9#$%^&*+=]{6,}',password):
    print ("Succes!")
else:
    print ("Self-destroying")
