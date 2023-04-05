"""
172. Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
Example 1:
Input: n = 3
Output: 0
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact=1
        count=0
        while n != 0:
            fact = fact*n
            n -= 1
        print(fact)
        s=str(fact)[::-1]
        print("test",s)
        for i in s:
            if i == "0":
                count += 1
            else:
                break
        print(count)
mysol =Solution()
mysol.trailingZeroes(n=7)