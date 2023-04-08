"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # mapp = {}
        # def dfs(node):
        #     if node in mapp:
        #         return mapp[node]
        #     copy = Node(node.val)
        #     mapp[node] = copy
        #     for n in node.neighbors:
        #         copy.neighbors.append(dfs(n))
        #     return copy
        # return dfs(node) if node else None
        
        if not node:
            return node

        repo = dict()
        repo[node] = Node(node.val)
        toProcess = deque([node])


        while toProcess:
            original = toProcess.pop()
            
            for on in original.neighbors:
                if on not in repo:
                    repo[on] = Node(on.val)
                    toProcess.append(on)

                cloned = repo.get(original)
                clonedN = repo.get(on)
                cloned.neighbors.append(
                    clonedN
                )
        return repo[node]