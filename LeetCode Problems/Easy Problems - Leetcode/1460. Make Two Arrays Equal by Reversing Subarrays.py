"""
You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray
 of arr and reverse it. You are allowed to make any number of steps.
Return true if you can make arr equal to target or false otherwise.
Example 1:
Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
"""


class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        from collections import Counter
        n,m = len(target),len(arr)
        if m > n:
            return False
        t = Counter(target)
        a = Counter(arr)
        for k,v in a.items():
            if k in t and v == t[k]:
                continue
            else:
                return False
        return True



mysol = Solution()
mysol.canBeEqual(target = [1,2,3,4], arr = [2,4,1,3])
