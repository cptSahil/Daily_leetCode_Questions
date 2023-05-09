class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while len(matrix)>0:
            res+=list(matrix[0])
            matrix = matrix[1:]
            matrix = list(zip(*matrix))
            matrix.reverse()
        return res