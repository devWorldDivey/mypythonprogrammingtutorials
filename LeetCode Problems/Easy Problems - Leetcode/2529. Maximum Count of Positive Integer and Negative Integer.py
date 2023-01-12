"""
2529. Maximum Count of Positive Integer and Negative Integer
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.



Example 1:

Input: nums = [-2,-1,-1,1,2,3]
Output: 3
"""
class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        pos,neg = 0,0
        for num in nums:
            if num > 0:
                pos += 1
            if num < 0:
                neg += 1
        print(pos, "----", neg)
        if pos > neg:
            return pos
        else:
            return neg


mysol = Solution()
mysol.maximumCount(nums = [-3,-2,-1,0,0,1,2])
