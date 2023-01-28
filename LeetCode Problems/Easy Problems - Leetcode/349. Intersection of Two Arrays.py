"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be
unique and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
"""
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        m1 = set(nums1)
        m2 = set(nums2)
        if len(m1)< len(m2):
            return [i for i in m1 if i in m2]
        else:
            return [i for i in m2 if i in m1]
mysol = Solution()
mysol.intersection(nums1 = [1,2,2,1], nums2 = [2,2])