class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        a = []
        b = []
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    a.append((i,j))
                if img2[i][j] == 1:
                    b.append((i,j))
        
        d = {}
        res = 0
        
        for a_x, a_y in a:
            for b_x, b_y in b:
                translation = (b_x-a_x, b_y-a_y)
                if translation in d:
                    d[translation] += 1
                else:
                    d[translation] = 1
                res = max(res,d[translation])
        return res