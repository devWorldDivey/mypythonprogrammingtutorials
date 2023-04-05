"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.
Example 1:

Input: x = 121
Output: true
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s[:] == s[::-1]:
            return True
        else:
            return False
mysol = Solution()
print(mysol.isPalindrome(x = -121))