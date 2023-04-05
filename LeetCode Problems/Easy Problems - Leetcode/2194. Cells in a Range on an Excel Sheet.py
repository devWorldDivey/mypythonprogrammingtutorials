"""
A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:
<col> denotes the column number c of the cell. It is represented by alphabetical letters.
For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
<row> is the row number r of the cell. The rth row is represented by the integer r.
You are given a string s in the format "<col1><row1>:<col2><row2>", where <col1>
represents the column c1, <row1> represents the row r1, <col2> represents the column
 c2, and <row2> represents the row r2, such that r1 <= r2 and c1 <= c2.

Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2.
The cells should be represented as strings in the format mentioned above and be sorted
 in non-decreasing order first by columns and then by rows.
"""
#Input: s = "K1:L2"
#Output: ["K1","K2","L1","L2"]
class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        out = []
        cell1,cell2 = s.split(":")
        print(cell1,cell2)
        col1 , row1 = cell1
        c,d = cell1
        print("character",c,"digit",d)
        print("column",col1,"row",row1)
        col2, row2 = cell2
        print(ord(col1))
        print(int(row1))
        for col in range(ord(col1),ord(col2)+1):
            for row in range(int(row1),int(row2)+1):
                cell = chr(col)+str(row)
                out.append(cell)
        return out
mysol = Solution()
mysol.cellsInRange(s = "K1:L2")