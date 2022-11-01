## initializing two lists
names = ['Harry', 'Emma', 'John']
ages = [19, 20, 18]

# zipping both
# zip() will return pairs of tuples with corresponding elements from both lists
print(dict(zip(names, ages)))