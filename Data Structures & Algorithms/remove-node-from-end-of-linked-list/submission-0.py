# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = ListNode(0, head)
        
        l = 0
        h = head
        while h:
            l += 1
            h = h.next

        h = s
        for i in range(l - n):
            h = h.next
        h.next = h.next.next

        return s.next