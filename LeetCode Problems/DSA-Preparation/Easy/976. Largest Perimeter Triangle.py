"""Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of
these lengths. If it is impossible to form any triangle of a non-zero area, return 0. """


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums = sorted(nums,reverse=True)
        perim = 0
        a,b,c =0,1,2
        while c < len(nums) and perim ==0:
            if (nums[a] + nums[b] > nums[c]) and (nums[a] + nums[c] > nums[b]) and (nums[b] + nums[c] > nums[a]):
                perim = nums[a] + nums[b] +nums[c]
            a += 1
            b += 1
            c += 1
        return perim


mysol = Solution()
print(mysol.largestPerimeter(nums=[1, 2, 1, 10]))
