# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        p1 = l1
        p2 = l2
        carry = 0
        while l1 or l2 or carry == 1:
            if carry == 1 and not l1 and not l2:
                a = self.add(0, 0, carry)
            elif not l2:
                a = self.add(l1.val, 0, carry)
                l1 = l1.next
            elif not l1:
                a = self.add(l2.val, 0, carry)
                l2 = l2.next
            else:
                a = self.add(l1.val, l2.val, carry)
                l1 = l1.next
                l2 = l2.next
            
            val = a[0]
            carry = a[1]

            curr.next = ListNode(val)
            curr = curr.next
        return head.next

    def add(self, n1, n2, carry):
        val = n1 + n2 + carry
        carry = 1 if val >= 10 else 0
        return (val % 10, carry)
