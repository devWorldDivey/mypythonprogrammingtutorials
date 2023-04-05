"""
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a
string s of length n where:
s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations
perm, return any of them.
Example 1:
Input: s = "IDID"
Output: [0,4,1,3,2]
"""


class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        n = len(s)
        d = 0
        res = []
        for i in s:
            if i == "I":
                res.append(n)
                n -= 1
            else:
                res.append(d)
                d+=1
        res.append(d)
        return res

mysol = Solution()
mysol.diStringMatch(s = "IDID")
