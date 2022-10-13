# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # if node.next==None:
        #     return 
        # else:
        #     node.val,node.next.val = node.next.val,node.val
        # temp = node.next
        # node.next = node.next.next
        # del(temp)
        # print(node)
        
        node.val=node.next.val
        node.next=node.next.next