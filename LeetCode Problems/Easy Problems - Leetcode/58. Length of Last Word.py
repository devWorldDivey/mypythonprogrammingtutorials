"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = []
        res = s.split()
        return len(res[-1])
mysol = Solution()
s = "Hello World"
mysol.lengthOfLastWord(s)
