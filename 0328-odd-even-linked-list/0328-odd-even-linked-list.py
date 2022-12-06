# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return 
        if head.next == None:
            return head

        odd, even = head, head.next
        while even and even.next:
            temp = even.next
            even.next = even.next.next

            temp.next = odd.next
            odd.next = temp

            odd, even = odd.next, even.next
        return head