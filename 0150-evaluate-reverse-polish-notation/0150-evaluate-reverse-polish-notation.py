class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        t = {'+','-','*','/'}
        for i in tokens:
            if i not in t:
                s.append(int(i))
            else:
                y,x = s.pop(),s.pop()
                if i == '+':
                    s.append(x+y)
                elif i == '-':
                    s.append(x-y)
                elif i == '*':
                    s.append(x*y)
                else:
                    s.append(trunc(x/y))
        return s[0]