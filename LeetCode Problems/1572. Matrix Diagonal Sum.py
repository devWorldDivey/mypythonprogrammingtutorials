"""
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Example 1:

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
"""
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]


class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        """
        primarysum = 0
        secondarysum = 0
        print(len(mat))
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j:
                    primarysum += mat[i][j]
                if i+j == len(mat)-1:
                    secondarysum += mat[i][j]
        if len(mat) % 2 == 0:
            return primarysum + secondarysum
        else:
            middle = len(mat) // 2
            return (primarysum + secondarysum) - mat[middle][middle]
        """
        primarysum = 0
        secondarysum = 0
        for i in range(len(mat)):
            primarysum += mat[i][i]
            secondarysum += mat[i][len(mat)-i-1]
        print(primarysum, "--",secondarysum)
        if len(mat) % 2 == 0:
            return primarysum +secondarysum
        else:
            middle = len(mat) // 2
            return (primarysum + secondarysum) - mat[middle][middle]

my_sol = Solution()
print(my_sol.diagonalSum(mat))