"""
Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1
 if such index does not exist.
x mod y denotes the remainder when x is divided by y.
Example 1:
Input: nums = [0,1,2]
Output: 0
"""
class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                print(i)
                return i
        return -1
mysol = Solution()
mysol.smallestEqual(nums=[4,5,6,9,9,5,9,0,8])