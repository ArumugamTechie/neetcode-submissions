class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}
        for r in range(0,9):
            rows[r] = rows.get(r,set())
            for c in range(0,9):
                cols[c] = cols.get(c,set())
                squares[(r//3,c//3)] = squares.get((r//3,c//3),set())
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3),(c//3)]) :
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3,c//3)].add(board[r][c])
        return True
        