"""
2373. Largest Local Values in a Matrix
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.
https://leetcode.com/problems/largest-local-values-in-a-matrix/
"""
grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]


class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        print(len(grid))


mysol1 = Solution()
mysol1.largestLocal(grid)