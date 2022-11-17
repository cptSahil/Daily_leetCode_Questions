class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        return (ax2-ax1)*(ay2-ay1)+(bx2-bx1)*(by2-by1)-self.cal(ax1,ax2,bx1,bx2)*self.cal(ay1,ay2,by1,by2)
    def cal(self,A1,B1,A2,B2):
        temp = min(B1,B2)-max(A1,A2)
        if temp<=0:
            return 0
        else:
            return temp