class Solution:
    def getSum(self, a: int, b: int) -> int:
        size = 0xffffffff
        while (b & size):
            s = a^b
            c = (a & b) << 1
            a = s
            b = c
        
        if b>0:
            return(a & size)
        return a