# How to open the file in Python and read the contents.
f = open("filehandlingdemo.txt")
contents = f.read()
print(contents)
f.close()
# Data Processing on File
file = open("filehandlingdemo.txt")
contents = file.read()
lines = contents.split("\n")
for line in lines:
    print(line)
    print("Number of character :", len(line))
    words = line.split()
    print("Number of words:", len(words))
file.close
# file manipulation using try except finally
try:
    file = open("filehandlingdemo.txt")
    file.read()
except Exception as e:
    print("Some error occurred:", e)
finally:
    file.close()
# Writing into File
fout = open("filehandlingdemo.txt", "w")  # Creating a new file if file doesnot exist
print("This is me", file=fout)
print("This is you", file=fout)
print("This is mine", file=fout)
print("This is yours", file=fout)
fout.close()
# Writing into File using append mode
fout = open("filehandlingdemo.txt", "a")
fout.write("My name is actually Divey Anand \n")
fout.write("Your name is Jyoti Gupta")
fout.close()
