# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p1 = head
        m = self.findMidPoint(head)
        p2 = self.reverseList(m.next)
        m.next = None

        while p2:
            next1 = p1.next
            next2 = p2.next

            p1.next = p2
            p2.next = next1

            p1 = next1
            p2 = next2
        
            
        

        
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        Next = head

        while curr != None:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next

        return prev

    def findMidPoint(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow