"""
The value of an alphanumeric string can be defined as:
The numeric representation of the string in base 10, if it comprises of digits only.
The length of the string, otherwise.
Given an array strs of alphanumeric strings, return the maximum value of any string in strs.
Example 1:
Input: strs = ["alic3","bob","3","4","00000"]
Output: 5
"""
class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        maxVal = 0
        for s in strs:
            if s.isdigit():
                maxVal = max(int(s),maxVal)
            else:
                maxVal = max(len(s),maxVal)
        return maxVal
mysol = Solution()
mysol.maximumValue(strs = ["alic3","bob","3","4","00000"])