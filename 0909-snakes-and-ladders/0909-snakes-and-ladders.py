class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        N_SQUARED = N*N
        visited = set()
        queue = deque([(1,0)])
        while queue:
            cur, steps = queue.popleft()
            if cur == N_SQUARED:
                return steps
            for nxt in range(cur + 1, min(cur + 6, N_SQUARED) + 1):
                if nxt not in visited:
                    visited.add(nxt)
                    d, m = divmod(nxt - 1, N)
                    r = N - d - 1
                    c = N - m - 1 if r % 2 == N % 2 else m
                    nxt_val = nxt if board[r][c] == -1 else board[r][c]
                    queue.append((nxt_val, steps + 1))
        return -1