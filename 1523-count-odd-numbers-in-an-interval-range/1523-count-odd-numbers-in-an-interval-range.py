class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high%2 == 1:
            h = (high+1)//2
        else:
            h = high//2
        if (low-1)%2 == 1:
            l = (low)//2
        else:
            l = (low-1)//2
        return h-l