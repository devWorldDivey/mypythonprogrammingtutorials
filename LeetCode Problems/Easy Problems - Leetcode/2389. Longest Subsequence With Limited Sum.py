"""
You are given an integer array nums of length n, and an integer array queries of length m.
Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can
 take from nums such that the sum of its elements is less than or equal to queries[i].
A subsequence is an array that can be derived from another array by deleting some or no elements
 without changing the order of the remaining elements.
Example 1:
Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
"""
class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        ans=[]
        nums.sort()
        for q in queries:
            s=0 #sum of subsequence
            l=0 #length of subsequence
            for i in nums:
                if s+i<=q: #check before adding the element.
                    s=s+i
                    l=l+1
                else:
                    break
            ans.append(l)
        return ans
mysol = Solution()
mysol.answerQueries(nums=[4,5,2,1],queries = [3,10,21])
