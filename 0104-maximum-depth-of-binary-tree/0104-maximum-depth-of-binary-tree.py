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

        def dfs(node, current_depth):
            nonlocal max_depth
            if not node:
                return
                
            if (node.left == None) and (node.right == None):
                max_depth = max(max_depth, current_depth)
            
            dfs(node.left, current_depth + 1)
            dfs(node.right, current_depth + 1)
        
        max_depth = 0
        dfs(root, 1)
        return max_depth