class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 : return s
        result = ''
        for i in range(numRows):
            increment = (numRows - 1)*2
            for j in range(i,len(s),increment):
                result += s[j]
                if i > 0 and i < numRows-1 and (j + increment - 2*i) < len(s):
                    result += s[j + increment - 2*i]
        return result