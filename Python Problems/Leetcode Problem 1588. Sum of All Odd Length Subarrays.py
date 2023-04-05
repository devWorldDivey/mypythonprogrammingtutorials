"""1588. Sum of All Odd Length Sub arrays Given an array of positive integers' arr, return the sum of all possible
odd-length sub arrays of arr. A subarray is a contiguous subsequence of the array.
Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

Link - https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
"""

arr = [1, 4, 2, 5, 3]


class Solution:
    def sumOddLengthSubArrays(self, arr: list[int]) -> int:
        """
        sum1 = 0
        for i in range(len(arr)):

            for j in range(i, len(arr), 2):
                print("i -", i, "j -", j)
                sum1 += sum(arr[i:j + 1])
                print("arr[i:j+1]-----",i,j+1,arr[i:j+1])
                print(sum1)
        return sum1
        """
        sum1 = 0
        subarr = []
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n + 1):
                # print(j)
                # subarr.append(arr[i:j])
                if (j-i)%2:
                    sum1 += sum(arr[i:j])
        print(sum1)


mySol1 = Solution()
print(mySol1.sumOddLengthSubArrays(arr))
