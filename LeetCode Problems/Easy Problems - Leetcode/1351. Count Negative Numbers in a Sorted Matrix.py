"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.
Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
"""

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        counter = 0
        for i in grid:
            for j in i:
                if j < 0:
                    counter += 1
        return counter

"""
using binary search
class Solution(object):
    def countNegatives(self, grid):
        def bin(row):
            start, end = 0, len(row)
            while start<end:
                mid = start +(end -start) // 2
                if row[mid]<0:
                    end = mid
                else:
                    start = mid+1
            return len(row)- start
        
        count = 0
        for row in grid:
            count += bin(row)
        return(count)
"""


mysol = Solution()
mysol.countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])