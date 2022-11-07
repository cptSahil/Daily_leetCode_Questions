class Solution:
    def maximum69Number (self, num: int) -> int:
        six = -1
        index = 0
        temp = num
        while temp:
            if temp%10==6:
                six = index
            temp //= 10
            index += 1
        if six != -1:
            return num + 3*10**six  
        else:
            return num
    