class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        
        adj = [list() for i in range(n)]
        for i in connections:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
            
        no_of_connected_components = 0
        visit = [False]*n
        for i in range(n):
            if not visit[i]:
                no_of_connected_components += 1
                self.bfs(i,adj,visit)
                
        return no_of_connected_components - 1
    
    def bfs(self,node,adj,visit):
        q = deque([node])
        visit[node] = True
        
        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if not visit[neighbor]:
                    visit[neighbor] = True
                    q.append(neighbor)