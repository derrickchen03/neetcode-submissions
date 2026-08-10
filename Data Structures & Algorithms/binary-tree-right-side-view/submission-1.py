# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        r = []
        while q:
            l = len(q)

            for i in range(l):
                a = q.popleft()
                if i == l - 1:
                    r.append(a.val)

                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
        return r