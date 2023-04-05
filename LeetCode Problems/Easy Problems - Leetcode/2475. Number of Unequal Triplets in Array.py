"""
You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the following conditions:

0 <= i < j < k < nums.length
nums[i], nums[j], and nums[k] are pairwise distinct.
In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
Return the number of triplets that meet the conditions.
"""
class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        myset = set(nums)
        print(len(myset)//3)
msol = Solution()
msol.unequalTriplets(nums = [1,2,3])