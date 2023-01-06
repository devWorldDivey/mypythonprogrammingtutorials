"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the
messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second
time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
mydict = {}
for lines in handle:
    lines.rstrip()
    words = lines.split()
    if len(words) > 0 and words[0] == "From":
        print(words[-2].split(":")[0])
        if words[-2].split(":")[0] not in mydict.keys():
            mydict[words[-2].split(":")[0]] = words[-2].split(":")[0].count(words[-2].split(":")[0])
        else:
            mydict[words[-2].split(":")[0]] += 1
for k,v in sorted(mydict.items()):
    print(k,v)
