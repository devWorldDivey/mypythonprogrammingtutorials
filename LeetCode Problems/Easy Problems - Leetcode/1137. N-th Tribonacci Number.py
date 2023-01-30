"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        for i in range(3,n+1):
            d = a + b + c
            a = b
            b = c
            c = d
        return d

mysol = Solution()
mysol.tribonacci(n=5)