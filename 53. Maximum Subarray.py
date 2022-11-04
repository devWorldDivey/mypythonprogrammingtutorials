"""
53. Maximum Subarray
Given an integer array nums, find the subarray which has the largest sum and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
nums = [-2, -1]


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        My Broot Force Solution

        class Solution:
        def maxSubArray(self, nums: List[int]) -> int:
        maxsum = 0
        for j in range(len(nums)):
            for k in range(j + 1, len(nums)):
                #print(nums[j:k], end="")
                if maxsum < sum(nums[j:k]):
                    maxsum = sum(nums[j:k])
            #print("\n")
        return maxsum

        """
        """Kadane's Algorithm is used for solving the problem
        This algorithm contains 3 steps----:
        Step1 Get the Sum at current and next index
        step2 Find the max of current Sum and previous sum
        step3 we need to check if sum is < 0 then again make it to zero again."""
        sumofnum = 0
        maxsum = nums[0]
        if len(nums) <= 1:
            sumofnum = nums[0]
        else:
            for i in range(len(nums)):
                sumofnum = sumofnum + nums[i]
                maxsum = max(maxsum, sumofnum)
                if sumofnum < 0:
                    sumofnum = 0
            print(maxsum)
            return maxsum


my_sol1 = Solution()
my_sol1.maxSubArray(nums)
