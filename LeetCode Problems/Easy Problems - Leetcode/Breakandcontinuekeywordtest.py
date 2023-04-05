"""
availablecandy = 5
x = int(input("Enter candy you want"))
i = 1
while i <= x:
    if i > availablecandy:
        print("Out of Stock")
        break
    print("Candy")
    i += 1
print("Bye")

#Continue

for i in range(1,101):
    if (i%2==0 or i%5==0):
        continue
    print(i)
print("Bye")
"""
#Pass
for i in range(1,101):
    if i%2==0:
        continue
        print(divey)
    else:
        print(i)

