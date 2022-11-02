"""1684. Count the Number of Consistent Strings
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent
if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
"""
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        count = 0
        for word in words:
            if sorted(set(word + allowed)) == sorted(allowed):
                print(sorted(set(word + allowed)) ,"==", sorted(allowed))
                count += 1
        print(count)


my_sol = Solution()
my_sol.countConsistentStrings(allowed,words)
