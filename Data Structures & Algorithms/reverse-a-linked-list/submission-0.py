# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        c = head
        f = head.next
        c.next = None
        while f.next:
            s = f.next
            f.next = c
            c = f
            f = s
        f.next = c
        return f