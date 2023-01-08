class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maxpt = 0
        n= len(points)
        for p1 in range (0,n):
            slopes = defaultdict(int)
            for p2 in range(p1+1,n):
                dy=(points[p2][1]-points[p1][1]) 
                dx=(points[p2][0]-points[p1][0])
                if dx!=0:
                    a=dy/ dx
                else: a=inf
                
                slopes[a]+= 1
                maxpt = max ( maxpt , slopes[a])
                    
        return maxpt+1