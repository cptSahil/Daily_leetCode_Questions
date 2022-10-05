# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        #BFS 
        if depth==1:
            node = TreeNode(val)
            node.left = root
            return node
        #depth!=1
        queue = [root]
        for i in range(depth-2):
            curr_len = len(queue)
            while curr_len>0:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                curr_len-=1
        for node in queue:
            temp_left = node.left
            temp_right = node.right
            node.left = TreeNode(val)
            node.right = TreeNode(val)
            node.left.left = temp_left
            node.right.right = temp_right
        return root
            
#         if depth == 1:
#             return TreeNode(val,root,None)
#         elif depth==2:
#             root.left = TreeNode(val,root.left,None)
#             root.right = TreeNode(val,None,root.right)
#         else:
#             if(root.left!=None):
#                 self.addOneRow(root.left,val,depth-1)
#             if(root.right!=None):
#                 self.addOneRow(root.right,val,depth-1)
#         return root