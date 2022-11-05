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
        n = len(grid)
        local_value = []

        for row in range(n-2):
            local_value.append([])
            for col in range(n-2):
                row_one = max(grid[row][col:col+3])
                row_two = max(grid[row+1][col:col+3])
                row_three = max(grid[row+2][col:col+3])

                max_local = max(row_one,row_two,row_three)
                local_value[row].append((max_local))
        print(local_value)

mysol1 = Solution()
mysol1.largestLocal(grid)
