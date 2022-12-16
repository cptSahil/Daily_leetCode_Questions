class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        l = len(num)
        for i in range(1,(l)//2+1):
            for j in range(1,(l-i)//2+1):
                a,b,c = num[:i],num[i:i+j],num[i+j:]
                if ((len(a)>1 and a[0]=="0") or (len(b)>1 and b[0]=="0")):
                    continue
                while c:
                    s = str(int(a)+int(b))
                    if s == c:
                        return True
                    if c.startswith(s):
                        a,b,c = (b,s,c[len(s):])
                    else:
                        break
        return False