class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        count = 0
        if n==0:
            return a
        elif n==1:
            return b
        elif n==2:
            return c
        else:
            for i in range(2,n):
                d = a+b+c
                a = b
                b = c
                c = d
            return d