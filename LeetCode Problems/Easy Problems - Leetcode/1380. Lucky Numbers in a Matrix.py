"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

"""
class Solution:
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        x = -1
        for value in [3, 41, 12, 9, 74, 15]:
            if value > x:
                x = value
        print(x)
        min_rows = [min(row) for row in matrix]
        max_cols = [max(col) for col in zip(*matrix)]
        return [num for num in min_rows if num in max_cols]
mysol = Solution()
print(mysol.luckyNumbers(matrix = [[3,7,8],
                             [9,11,13],
                             [15,16,17]]))