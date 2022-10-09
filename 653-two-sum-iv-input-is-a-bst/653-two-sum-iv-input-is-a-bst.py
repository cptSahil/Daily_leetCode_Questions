# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        h = set()
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                continue
            if k-node.val in h:
                return True
            h.add(node.val)
            q.append(node.left)
            q.append(node.right)
        return False