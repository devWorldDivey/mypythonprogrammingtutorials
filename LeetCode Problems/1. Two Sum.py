"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
nums = [11, 15, 2, 7]
target = 9


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict1 = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j not in dict1.keys():
                dict1.update({nums[i]: nums.index(nums[i])})
            else:
                return [dict1.get(j), i]


my_sol1 = Solution()
print(my_sol1.twoSum(nums, target))
