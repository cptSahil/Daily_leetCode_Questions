class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        temp = [1]+[0]*(len(obstacleGrid[0])-1)
        
        for row in obstacleGrid:
            curr = []
            for i, obstacle in enumerate(row):
                if obstacle:
                    curr.append(0)
                else:
                    curr.append(temp[i]+(curr[-1] if curr else 0))
            temp = curr
        return temp[-1]
        
        