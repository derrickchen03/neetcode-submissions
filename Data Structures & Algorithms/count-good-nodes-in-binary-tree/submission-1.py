# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        g = 0
        def dfs(root, cm):
            nonlocal g
            if not root:
                return
            if root.val >= cm:
                g += 1
                dfs(root.left, root.val)
                dfs(root.right, root.val)
            else:
                dfs(root.left, cm)
                dfs(root.right, cm)
        if root:
            dfs(root, root.val)
        return g
