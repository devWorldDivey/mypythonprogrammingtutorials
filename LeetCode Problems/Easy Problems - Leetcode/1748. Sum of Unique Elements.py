"""
You are given an integer array nums. The unique elements of an array are the elements that appear exactly
once in the array.Return the sum of all the unique elements of nums.
Input: nums = [1,2,3,2]
Output: 4
"""
class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        res = []
        for i in nums:
            if nums.count(i) == 1:
               res.append(i)
        return sum(res)


mysol = Solution()
print(mysol.sumOfUnique(nums = [1,2,3,2]))
