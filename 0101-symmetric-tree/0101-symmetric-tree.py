# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            if left.val == right.val:
                outer = mirror(left.left, right.right)
                inner = mirror(left.right, right.left)
                return outer and inner
            else:
                return False
            
        if not root:
            return True
        else:
            return mirror(root.left, root.right)
    