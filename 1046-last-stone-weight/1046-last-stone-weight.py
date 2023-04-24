class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        else:
            stones.sort(reverse=True)
            while len(stones)>1:
                i = 0
                j = 1
                if stones[i]==stones[j]:
                    stones.remove(stones[i])
                    stones.remove(stones[i])
                    if len(stones)==0:
                        return 0
                else:
                    stones[i]=(abs(stones[i]-stones[j]))
                    stones.remove(stones[j])
                    stones.sort(reverse=True)
        return stones[0]