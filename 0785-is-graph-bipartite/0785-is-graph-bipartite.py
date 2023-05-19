from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        
        for node in range(n):
            if color[node] == -1:
                if not self.dfs(graph, node, color, 0):
                    return False
        return True

    def dfs(self, graph, node, color, curr_color):
        color[node] = curr_color
        
        for neighbor in graph[node]:
            if color[neighbor] == curr_color:
                return False
            if color[neighbor] == -1 and not self.dfs(graph, neighbor, color, 1 - curr_color):
                return False
            
        return True