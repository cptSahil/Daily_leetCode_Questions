# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maximum_depth = 0
        if root == None:
            return maximum_depth
        queue = deque([])
        queue.append(root)
        while len(queue) != 0:
            maximum_depth += 1
            level_size = len(queue)
            for i in range(level_size):
                current = queue.popleft()
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
        return maximum_depth
    
    
    