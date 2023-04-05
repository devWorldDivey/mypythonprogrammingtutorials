"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dict = {}
        for i in nums:
            if nums.count(i) == 1:
                return i

mysol = Solution()
mysol.singleNumber(nums = [2,2,1])