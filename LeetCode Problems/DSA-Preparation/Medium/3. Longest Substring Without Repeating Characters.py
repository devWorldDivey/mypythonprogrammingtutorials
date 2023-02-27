"""
Given a string s, find the length of the longest substring without repeating characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                res.append(s[i:j])

        print(res)

print(a=10)
print(a="abcd")
