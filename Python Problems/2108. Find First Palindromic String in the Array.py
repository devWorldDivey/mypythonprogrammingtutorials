"""
2108. Find First Palindromic String in the Array
Given an array of strings words, return the first palindromic string in the array.
If there is no such string, return an empty string "".
A string is palindromic if it reads the same forward and backward.
Example 1:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
"""
class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for i in words:
            #print(i)
            i = list(i)
            #print(i)
            rev = i[::-1]
            if i == rev:
                return i
        return ""



words = ["abc","car","ada","racecar","cool"]
mysol = Solution()
mysol.firstPalindrome(words)

a = ["a","b","c"]
print(a[1])
print(a[1:])
print(a[:1])
print(a[::-1])
