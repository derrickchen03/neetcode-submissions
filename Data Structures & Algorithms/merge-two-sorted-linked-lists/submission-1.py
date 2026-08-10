# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        if not p1:
            return p2
        elif not p2:
            return p1
        h = ListNode()
        trav = h

        while p1 and p2:
            if p1.val < p2.val:
                trav.next = p1
                p1 = p1.next
            else:
                trav.next = p2
                p2 = p2.next
            trav = trav.next
        if not p1:
            trav.next = p2
        elif not p2:
            trav.next = p1

        return h.next