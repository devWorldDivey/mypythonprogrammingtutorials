"""
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has
(also known as the Hamming weight).
Note:
Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given
as a signed integer type. It should not affect your implementation, as the integer's internal binary representation
is the same, whether it is signed or unsigned. In Java, the compiler represents the signed integers using 2's
complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n.bit_count())

    def subtractProductAndSum(self, n: int) -> int:
        print(eval('*'.join(str(n))))
        print(eval('*'.join(str(n))) - eval('+'.join(str(n))))

mysol = Solution()
mysol.hammingWeight(n = 234)
mysol.subtractProductAndSum(n=234)

"""
1281. Subtract the Product and Sum of Digits of an Integer
"""