class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        res = [1]*n
        l = []
        for i,j in enumerate(obstacles):
            idx = bisect.bisect_right(l,j)
            if idx == len(l):
                l.append(j)
            else:
                l[idx] = j
            res[i] = idx + 1
        return res