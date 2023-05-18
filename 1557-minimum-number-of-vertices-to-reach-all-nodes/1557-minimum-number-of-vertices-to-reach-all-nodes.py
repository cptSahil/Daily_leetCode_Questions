class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        isIncomingEdgeExists = [False] * n

        for edge in edges:
            isIncomingEdgeExists[edge[1]] = True
        
        requiredNodes = []

        for vertex, value in enumerate(isIncomingEdgeExists):
            if not value:
                requiredNodes.append(vertex)
        
        return requiredNodes