"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {None: None}
        h = head

        
        while h:
            d[h] = Node(h.val)
            h = h.next

        h = head
        while h:
            x = d[h]
            x.next = d[h.next]
            x.random = d[h.random]
            h = h.next
        return d[head]

