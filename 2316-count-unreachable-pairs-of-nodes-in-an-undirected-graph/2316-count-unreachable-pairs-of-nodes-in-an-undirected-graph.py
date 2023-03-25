class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def count(node):
            if node in visited:
                return 0
            visited.add(node)
            return sum(count(i) for i in adj_list[node]) + 1
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        return sum((size := count(i)) * (n - size) for i in range(n) if i not in visited) // 2