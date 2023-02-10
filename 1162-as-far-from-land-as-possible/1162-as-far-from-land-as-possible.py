class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        queue = []
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue.append((r,c,0))
        if len(queue) == rows*cols or len(queue) == 0:
            return -1
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        maximum = 1
        
        while queue:
            nr,nc,nd = queue.pop(0)
            for dirs in directions:
                dr,dc = dirs
                new_r, new_c = nr+dr,nc+dc
                if rows-1>=new_r>=0 and cols-1>=new_c>=0 and grid[new_r][new_c] == 0:
                    queue.append((new_r,new_c,nd+1))
                    grid[new_r][new_c] = nd+1
                    maximum = max(maximum,nd+1)
        return maximum