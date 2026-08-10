"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        h = {}
        def dfs(node: Optional['Node']):
            if node in h:
                return h[node]

            a = Node(node.val)
            h[node] = a

            for n in node.neighbors:
                a.neighbors.append(dfs(n))

            return a
        return dfs(node)