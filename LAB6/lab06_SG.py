import re
password = input("Please enter a password")
if re.search(r'[A-Za-z0-9#$%^&*+=\-\_\!]{6,}',password):
    print ("Success!")
else:
    print ("Self-destroying")
