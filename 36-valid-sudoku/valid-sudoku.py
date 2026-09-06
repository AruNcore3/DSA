class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowSet = set()
            for j in range(9):
                num = board[i][j]
                if num in rowSet:return False
                elif num != '.':rowSet.add(num)

        for i in range(9):
            colSet = set()
            for j in range(9):
                num = board[j][i]
                if num in colSet:return False
                elif num != '.':colSet.add(num)
        
        starting_pos = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]

        for i_start,j_start in starting_pos:
            s = set()
            for i in range(i_start,i_start+3):
                for j in range(j_start,j_start+3):
                    num = board[i][j]
                    if num  in s:return False
                    elif num != '.':s.add(num)

        return True