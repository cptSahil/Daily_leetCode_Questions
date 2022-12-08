class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dir = [[1]*m for _ in range(n)]
        
        for i in range(1,n):
            for j in range(1,m):
                dir[i][j] = dir[i-1][j] + dir[i][j-1]
                
        return dir[-1][-1]