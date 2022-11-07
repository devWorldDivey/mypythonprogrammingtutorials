"""
350. Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear
as many times as it shows in both arrays and you may return the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""
nums1 = [1, 2, 2, 1]
nums2 = [2,2]


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        j = 0
        for i in range(len(nums1)-1):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                if len(nums2) < j:
                    j += 1
                else:
                    break
        return res


my_sol = Solution()
print(my_sol.intersect(nums1, nums2))
