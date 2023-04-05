"""
You are given a string s of even length. Split this string into two halves of equal lengths, and
let a be the first half and b be the second half.
Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
Notice that s contains uppercase and lowercase letters.
Return true if a and b are alike. Otherwise, return false.
Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        ch = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        n = len(s)
        fst, sec = 0, 0
        for i in range(n):
            if i < n // 2:
                if s[i] in ch:
                    fst += 1
            else:
                if s[i] in ch:
                    sec += 1
        return fst == sec



mysol = Solution()
mysol.halvesAreAlike(s="textbook")
