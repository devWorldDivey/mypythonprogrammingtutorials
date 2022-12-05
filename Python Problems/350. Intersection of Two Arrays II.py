"""
350. Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear
as many times as it shows in both arrays and you may return the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""
nums1 = [54, 93, 21, 73, 84, 60, 18, 62, 59, 89, 83, 89, 25, 39, 41, 55, 78, 27, 65, 82, 94, 61, 12, 38, 76, 5, 35, 6,
         51, 48, 61, 0, 47, 60, 84, 9, 13, 28, 38, 21, 55, 37, 4, 67, 64, 86, 45, 33, 41]
nums2 = [17, 17, 87, 98, 18, 53, 2, 69, 74, 73, 20, 85, 59, 89, 84, 91, 84, 34, 44, 48, 20, 42, 68, 84, 8, 54, 66, 62,
         69, 52, 67, 27, 87, 49, 92, 14, 92, 53, 22, 90, 60, 14, 8, 71, 0, 61, 94, 1, 22, 84, 10, 55, 55, 60, 98, 76,
         27, 35, 84, 28, 4, 2, 9, 44, 86, 12, 17, 89, 35, 68, 17, 41, 21, 65, 59, 86, 42, 53, 0, 33, 80, 20]


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dict1 = {}
        res = []
        for i in range(len(nums1)):

            if nums1[i] not in dict1.keys():
                dict1.update({nums1[i]: nums1.count(nums1[i])})
        print(dict1)
        for j in range(len(nums2)):
            if nums2[j] in dict1.keys():
                if dict1.get(nums2[j]) > 0:
                    dict1.update({nums2[j]: dict1.get(nums2[j]) - 1})
                    res.append(nums2[j])
        print(res)


my_sol = Solution()
print(my_sol.intersect(nums1, nums2))
