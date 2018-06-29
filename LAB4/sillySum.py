import math
import os
file = open("results.txt","w+")
if not os.path.isfile(file):
    print("File not found!\n")
    exit(1)
with open('numbers.txt','r') as input:
    for line in input:
        num = int(line)
        sqrt = math.sqrt(num)
        exp = num**2
        sum = sqrt + exp
        file.write(str(sum) + "\n")
    file.close()
print("done")
