import math
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxsum = -math.inf
        sum = 0
        for i in nums:
            sum += i
            maxsum = max(maxsum,sum)
            if sum < 0:
                sum = 0
        print(maxsum)
                
mysol = Solution()
mysol.maxSubArray(nums = [-1])