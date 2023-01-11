"""
2500. Delete Greatest Value in Each Row
You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.
Input: grid = [[1,2,4],[3,3,1]]
Output: 8
"""
class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        length = len(grid)
        result = 0
        while True:
            if len(grid[0])==0:
                break
            current_max = []
            for row in range(length):
                max_element = max(grid[row])
                grid[row].remove(max_element)
                current_max.append(max_element)
            result += max(current_max)
        print(result)
        return result
mysol = Solution()
mysol.deleteGreatestValue(grid = [[1,2,4],[3,3,1]])

