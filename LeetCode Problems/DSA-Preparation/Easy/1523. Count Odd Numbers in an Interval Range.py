"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).



Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
"""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = 0
        if low%2 != 0:
            ans += 1
        elif high%2 != 0:
            ans += 1
        print(ans + (high-low)//2)
mysol = Solution()
mysol.countOdds(3,7)