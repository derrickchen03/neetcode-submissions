# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c = 0
        x = 0
        def dfs(root):
            nonlocal c, k, x
            if not root:
                return
            dfs(root.left)
            c += 1

            if c == k:
                x = root.val
            
            dfs(root.right)
        dfs(root)
        return x
            