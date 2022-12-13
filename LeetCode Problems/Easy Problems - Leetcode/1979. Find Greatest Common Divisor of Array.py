"""
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.



Example 1:

Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
"""
class Solution:
    def findGCD(self, nums: list[int]) -> int:
        l = max(nums)
        m = min(nums)
        res = []
        if l%m == 0:
            return m
        else:
            for i in range(1,m+1):
                if (l % i)==0 and (m % i)==0:
                    res.append(i)
            return max(res)


mysol = Solution()
mysol.findGCD(nums = [7,5,6,8,3])