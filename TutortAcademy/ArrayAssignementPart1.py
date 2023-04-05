# 1. https://leetcode.com/problems/two-sum/ 
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Solved in O(n) using Dictionary in python
        sol_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in sol_dict:
                sol_dict[nums[i]] = i
            else:
                return [sol_dict[diff],i]


#2. https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
    def twoSum1(self, numbers: list[int], target: int) -> list[int]:
        i = 0 
        j = len(numbers)-1
        while i <= j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1   
            else:             
                j -= 1

#3. https://leetcode.com/problems/merge-sorted-array/




# Object and method calling
mysol = Solution()
mysol.twoSum([2,7,11,15], target = 9)
print(mysol.twoSum1([2,7,11,15], target = 9))