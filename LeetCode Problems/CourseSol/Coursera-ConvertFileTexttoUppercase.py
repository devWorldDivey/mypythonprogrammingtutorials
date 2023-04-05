# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
print(fh)
for i in fh:
    i = i.rstrip()
    print(i.upper())
