class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        def is_safe(x, y, val):
            for i in range(n):
                if board[i][y] == val and i != x:
                    return False
            print('safe col')
            for i in range(n):
                if board[x][i] == val and i != y:
                    return False
            print('safe row')
            rows = x - x % 3
            cols = y - y % 3
            for i in range(3):
                for j in range(3):
                    if board[i+rows][j+cols] == val and i+rows != x and j+cols != y:
                        return False
            return True
        for row in range(9):
            for col in range(9):
                cur = board[row][col]
                if cur == '.':
                    continue
                if not is_safe(row, col, board[row][col]):
                    return False
        return True