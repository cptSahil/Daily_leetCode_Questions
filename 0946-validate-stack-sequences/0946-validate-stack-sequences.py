class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        x = 0
        for i in pushed:
            s.append(i)
            while s and s[-1]==popped[x]:
                s.pop()
                x+=1
        if s:
            return False
        return True