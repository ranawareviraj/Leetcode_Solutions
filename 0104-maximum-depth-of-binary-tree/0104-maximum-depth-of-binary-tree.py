# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_in_left = self.maxDepth(root.left)
        max_in_right = self.maxDepth(root.right)

        return 1 + max(max_in_left, max_in_right)