""" Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j
    such that |nums[i] - nums[j]| == k.
Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
    https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
"""

nums = [1, 2, 2, 1]
k = 1


class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                print(nums[j], "-", nums[i])
                if k == abs(nums[j] - nums[i]):
                    count += 1
        print(count)


my_sol = Solution()
my_sol.countKDifference(nums, k)
