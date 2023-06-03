class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = [[] for _ in range(len(manager))]
        root = -1
        for i in range(len(manager)):
            if manager[i] == -1:
                root = i
            elif manager[i] != -1:
                tree[manager[i]].append(i)

        bfs = []
        bfs.append([root, 0])
        result = -1
        while len(bfs) != 0:
            current = bfs.pop(0)
            if current[1] > result:
                result = current[1]
            for i in range(len(tree[current[0]])):
                bfs.append([tree[current[0]][i], current[1] + informTime[current[0]]])

        return result