# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(r, sr):
            if not r or not sr:
                return False
            return sub(r, sr) or dfs(r.left, sr) or dfs(r.right, sr)
            
        def sub(r, sr):
            if not r and not sr:
                return True
            elif (not r and sr) or (r and not sr):
                return False
            if r.val == sr.val:
                return sub(r.left, sr.left) and sub(r.right, sr.right)
            return False
            
        if not root or not subRoot:
            return False
        return dfs(root, subRoot)
