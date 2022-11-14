class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        
        xs = collections.defaultdict(list)
        ys = collections.defaultdict(list)
        
        for index,(x,y) in enumerate(stones):
            xs[x].append(index)
            ys[y].append(index)
        
        def go(index):
            count = 1
            done[index] = True
            
            x,y = stones[index]
            if x in xs:
                L = xs[x]
                del xs[x]
                for j in L:
                    if not done[j]:
                        count += go(j)
    
            if y in ys:
                L = ys[y]
                del ys[y]
                for j in L:
                    if not done[j]:
                        count += go(j)
            return count
            
        
        total = 0 
        done = [False]*N
        for index,(x,y) in enumerate(stones):
            if not done[index]:
                total += go(index)-1
        return total