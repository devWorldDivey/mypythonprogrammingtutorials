"""
2367. Number of Arithmetic Triplets
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.

"""


"""
class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        print(nums, "---", diff)
        count = 0
        for i in nums:
            if i + diff in nums:
                if i + diff + diff in nums:
                    count += 1
        print(count)
"""
nums = [4, 5, 6, 7, 8, 9]
diff = 2


class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        pass


mySol1 = Solution()
mySol1.arithmeticTriplets(nums, diff)
