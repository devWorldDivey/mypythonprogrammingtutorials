"""
Given a string s and a character c that occurs in s, return an array of integers answer where answer.
length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
Example 1:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
"""
import itertools


class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = lastC = len(s)
        ans = [n]*n
        for i in itertools.chain(range(n),range(n)[::-1]):
            if s[i]==c:
                lastC = i
            ans[i]=min(ans[i],abs(i-lastC))
        print(ans)
mysol = Solution()
mysol.shortestToChar(s = "loveleetcode", c = "e")