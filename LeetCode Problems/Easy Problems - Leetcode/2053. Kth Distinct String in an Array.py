"""
A distinct string is a string that is present only once in an array.
Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are
fewer than k distinct strings, return an empty string "".
Note that the strings are considered in the order in which they appear in the array.
Example 1:
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
"""
class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        from collections import Counter
        l = []
        x = Counter(arr)
        print(x)
        for i, j in x.items():
            if j == 1:
                l.append(i)
        if len(l) < k:
            return ""
        return l[k - 1]
mysol = Solution()
mysol.kthDistinct(arr = ["d","b","c","b","c","a"], k = 2)