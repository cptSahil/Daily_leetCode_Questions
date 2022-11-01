class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        m, n = len(grid), len(grid[0])
        ans = []
        for col in range(n):
            cur_col = col
            for cur_row in range(m):
                next_col = cur_col + grid[cur_row][cur_col]
                if next_col < 0 or next_col >= n or grid[cur_row][cur_col] ^ grid[cur_row][next_col]:
                    cur_col = -1
                    break
                cur_col = next_col
            ans.append(cur_col)
        return ans