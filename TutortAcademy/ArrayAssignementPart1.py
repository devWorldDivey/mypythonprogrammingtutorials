# 1. https://leetcode.com/problems/two-sum/ 
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Solved in O(n) using Dictionary in python
        sol_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in sol_dict:
                sol_dict[nums[i]] = i
            else:
                return [sol_dict[diff],i]
mysol = Solution()
mysol.twoSum([2,7,11,15], target = 9)