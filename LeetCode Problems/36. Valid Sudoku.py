"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
board =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # check validity for each row
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j].isdigit() and board[i][j] in s: return False
                s.add(board[i][j])

            # check validity for each column
        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j].isdigit() and board[i][j] in s: return False
                s.add(board[i][j])

            # check validity for 3x3 matrix
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l].isdigit() and board[k][l] in s: return False
                        s.add(board[k][l])

        return True


mysol = Solution()
mysol.isValidSudoku(board)
