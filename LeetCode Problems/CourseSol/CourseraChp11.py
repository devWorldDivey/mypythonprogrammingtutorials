import re
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "regex_sum_1648071.txt"

fh = open(fname)
counter = 0
numlist,res = list(),list()
for lines in fh:
    numlist = re.findall( '[0-9]+',lines)
    if len(numlist) > 0:
        res.append((numlist))
for i in res:
    for j in i:

        counter += int(j)
print(counter)