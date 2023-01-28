"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']'}
        m = []
        for i in s:
            if i in d:
                m.append(i)
            else:
                if len(m) and d[m[-1]] == i:
                    del m[-1]
                else:
                    return False
        return not m


mysol = Solution()
mysol.isValid(s="()[]{}")
