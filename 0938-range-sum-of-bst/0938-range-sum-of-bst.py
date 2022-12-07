# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        if root == None:
            return 0
        
        q = deque()
        q.append(root)
        while(len(q)>0):
            curr = q.popleft()
            if(curr.val >= low and curr.val <= high):
                sum += curr.val
            if(curr.left != None and curr.val > low):
                q.append(curr.left)
            if(curr.right != None and curr.val < high):
                q.append(curr.right)
        return sum