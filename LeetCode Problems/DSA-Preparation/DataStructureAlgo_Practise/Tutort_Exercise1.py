"""Q1. Q1. Given an array of N integers. Your task is to print the sum of all the integers.
Example 1:
Input:
4
1 2 3 4
Output:
10
Example 2:
Input:
6
5 8 3 10 22 45
Output:
93
"""
class Solution:
    def getsum(self, nums: list[int]) -> int:
        sumc =0
        for i in nums:
            sumc += i
        print(sumc)
mysol = Solution()
mysol.getsum([5,8,3,10,22,45])

