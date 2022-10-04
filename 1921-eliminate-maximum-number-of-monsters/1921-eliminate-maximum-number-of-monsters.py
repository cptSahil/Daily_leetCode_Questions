class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        d = []
        
        for i in range(len(dist)):
            d.append(dist[i]/speed[i])
        d.sort()
        remaining_time = 0
        monsters = 0
        
        for i in d:
            if i-remaining_time<=0:
                return monsters
            remaining_time += 1
            monsters += 1
        return monsters