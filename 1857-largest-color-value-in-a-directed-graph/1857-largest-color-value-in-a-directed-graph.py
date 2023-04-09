class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        colors = [ord(c) - 97 for c in colors]
        
        adj_list = defaultdict(list)
        indegree = [0]*n
        for u,v in edges:
            adj_list[u].append(v)
            indegree[v]+=1
            
        queue = deque()
        for node in range(n):
            if indegree[node] == 0:
                queue.append((node))
                
        counter = [[0]*26 for _ in range(n)]
        
        max_len = 1
        processed = 0
        while queue:
            node = queue.popleft()
            counter[node][colors[node]] += 1
            max_len = max(max_len, counter[node][colors[node]])
            processed += 1
            for nei in adj_list[node]:
                for i in range(26):
                    counter[nei][i] = max(counter[nei][i], counter[node][i])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append((nei))
        return max_len if processed == n else -1