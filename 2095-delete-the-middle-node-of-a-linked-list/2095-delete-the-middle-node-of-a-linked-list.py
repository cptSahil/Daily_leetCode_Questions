# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        prev = None
        while(fast!=None and fast.next!=None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev == None:
            return None
        prev.next = slow.next
        return head
        