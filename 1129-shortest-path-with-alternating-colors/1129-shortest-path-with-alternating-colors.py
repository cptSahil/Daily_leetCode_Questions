class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for src, dest in redEdges:
            adj[src].append((dest, 0)) 
        for src, dest in blueEdges:
            adj[src].append((dest, 1)) 

        res = [-1]*n
        res[0] = 0

        visited = [[False, False] for _ in range(n)]
        visited[0][0] = visited[0][1] = True
            
        # node, steps, last_color
        queue = deque()
        queue.append((0, 0, 0))
        queue.append((0, 0, 1))
        
        while queue:
            node, steps, last_color = queue.popleft()
            for nei, col in adj[node]:
                if (col != last_color) and (visited[nei][col] == False):
                    if res[nei] == -1:
                        res[nei] = steps+1
                    visited[nei][col] = True
                    queue.append((nei, steps+1, col))

        return res