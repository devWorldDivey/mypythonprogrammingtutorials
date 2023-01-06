"""
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start
 with an empty record.You are given a list of strings operations, where operations[i] is the ith operation
 you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.
The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer
 and that all operations are valid.
Example 1:
Input: ops = ["5","2","C","D","+"]
Output: 30
"""


class Solution:
    def calPoints(self, operations: list[str]) -> int:
        p = []
        for i in operations:
            if i == 'C':
                p.pop()
            elif i == 'D':
                p.append(2 * p[-1])
            elif i == '+':
                p.append(p[-1] + p[-2])
            else:
                p.append(int(i))
        return sum(p)


mysol = Solution()
print(mysol.calPoints(operations = ["5","2","C","D","+"]))