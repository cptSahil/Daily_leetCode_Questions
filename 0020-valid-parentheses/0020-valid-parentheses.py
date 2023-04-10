class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        for i in s:
            if i not in d:
                stack.append(i)
            elif not stack or d[i]!= stack[-1]:
                return False
            else:
                stack.pop()
        return not stack