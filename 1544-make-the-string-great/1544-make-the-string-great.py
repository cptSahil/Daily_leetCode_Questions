class Solution:
    def makeGood(self, s: str) -> str:
        l = []
        for char in s:
            if l and l[-1]==char.swapcase():
                l.pop()
            else:
                l.append(char)
        return "".join(l)
        