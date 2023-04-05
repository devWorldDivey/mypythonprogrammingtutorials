"""
Given an array of integers nums, half of the integers in nums are odd, and the other
half are even.
Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even,
 i is even.
Return any answer array that satisfies this condition.
Example 1:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
"""
class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        queue = []
        even = [i for i in nums if i%2 == 0]
        odd = [i for i in nums if i%2 != 0]

        for a,b in zip(even,odd):
            queue.append(a)
            queue.append(b)
        return queue


mysol = Solution()
mysol.sortArrayByParityII(nums=[4,2,5,7])