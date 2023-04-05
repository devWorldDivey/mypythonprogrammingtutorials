"""
You are given an integer array arr. Sort the integers in the array in ascending order by the number
 of 1's in their binary representation and in case of two or more integers have the same number of
 1's you have to sort them in ascending order.
Return the array after sorting it.
Example 1:
Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
"""
class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        arr = sorted(arr)
        # Create a list of tuples (num, num_ones)
        nums_with_ones = [(num, bin(num).count('1')) for num in arr]
        print(nums_with_ones)
        # Sort the list of tuples by the number of 1s
        nums_with_ones.sort(key=lambda x: x[1])
        print(nums_with_ones)
        # Extract the sorted list of integers
        return [num for num, num_ones in nums_with_ones]

mysol = Solution()
print(mysol.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1]))