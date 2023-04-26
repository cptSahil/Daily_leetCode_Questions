class Solution:
    def addDigits(self, num: int) -> int:
        root = 0
        while num>0:
            root += num % 10
            num = num // 10
            
            if num == 0 and root > 9:
                num = root
                root = 0
        return root