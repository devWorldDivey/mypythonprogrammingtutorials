"""
You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums.

You then do the following steps:

If original is found in nums, multiply it by two (i.e., set original = 2 * original).
Otherwise, stop the process.
Repeat this process with the new number as long as you keep finding the number.
Return the final value of original.



Example 1:

Input: nums = [5,3,6,1,12], original = 3
Output: 24
"""
class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        if original in nums:
            self.findFinalValue(nums,original *2)
        else:
            return original



mysol = Solution()
print(mysol.findFinalValue(nums = [5,3,6,1,12], original = 3))


