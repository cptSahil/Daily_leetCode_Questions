class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(set)
        for u,v in connections:
            adj[u].add((v,True))
            adj[v].add((u,False))
            
        queue = deque([0])
        visited = set([0])
        
        change = 0
        while queue:
            node = queue.popleft()
            
            for i,j in adj[node]:
                if i not in visited:
                    change += j
                    queue.append(i)
                    visited.add(i)
        return change