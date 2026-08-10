# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def maxDepth(node):
            nonlocal answer
            if not node:
                return 0
            l = maxDepth(node.left)
            r = maxDepth(node.right)

            answer = max(answer, l + r)
            return max(l,r) + 1
        maxDepth(root)
        return answer
        