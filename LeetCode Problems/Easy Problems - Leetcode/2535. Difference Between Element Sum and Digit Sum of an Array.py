"""
You are given a positive integer array nums.The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.
Note that the absolute difference between two integers x and y is defined as |x - y|.
Example 1:
Input: nums = [1,15,6,3]
Output: 9
"""
class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        elementsum = sum(nums)
        digitsum = 0
        for i in nums:
            stri = str(i)
            for j in stri:
                digitsum += int(j)
        print(abs(elementsum-digitsum))
mysol = Solution()
mysol.differenceOfSum(nums = [1,15,6,3])
