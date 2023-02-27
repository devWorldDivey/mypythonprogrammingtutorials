nums = [3,2,3,4]
print("--->",nums[0:3])
maxp = 0
for i in range(len(nums)):
    for j in range(i+3,len(nums)+1):
        print(nums[i:j])

