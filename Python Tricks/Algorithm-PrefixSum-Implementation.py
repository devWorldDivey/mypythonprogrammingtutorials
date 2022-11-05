# Prefix Sum is a powerful algorithm to do problem 2367 of Leet code - Number of Arithmetic Triplets
arr = [0, 1, 2, 3, 4, 5]
res = []
for i in range(len(arr)):
    if i == 0:
        res.append(arr[i])
    if i < len(arr)-1:
        res.append(res[i]+arr[i+1])
print(res)

