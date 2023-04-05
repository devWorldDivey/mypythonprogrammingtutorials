"""
2206. Divide Array Into Equal Pairs
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.
"""
nums = [18,19,5,5,18,19,5,6,12,19,13,4,16,11,4,16,10,8,12,8,2,1,8,17,4,18,3,5,16,2,16,12,17,16,7,16,2,17,19,9,1,20,17,17,4,6]
class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        mydict = {}
        numset = set(nums)
        mycheck = True
        for i in numset:
            mydict[i]=nums.count(i)
        for key in mydict:
            if mydict[key] % 2 != 0:
                mycheck=False
        return mycheck
        print(mydict)

mysol = Solution()
mysol.divideArray(nums)
