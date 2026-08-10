
class ll:
    def __init__(self, key: None, val: None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}

        self.head = ll(0,0)
        self.tail = ll(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]  
            self.remove(node)
            self.add(node)
            return node.val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        
        node = ll(key, value)
        self.add(node)
        self.d[key] = node

        if len(self.d) > self.capacity:
            r = self.tail.prev
            self.remove(r)
            del self.d[r.key]
            
        

    def add(self, node: ll) -> None:
        nex = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = nex
        nex.prev = node


    def remove(self, node: ll) -> None:
        prev = node.prev
        nex = node.next

        prev.next = nex
        nex.prev = prev