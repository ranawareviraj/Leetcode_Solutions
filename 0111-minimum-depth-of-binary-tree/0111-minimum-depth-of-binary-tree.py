# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node, depth):
            nonlocal min_depth
            if not node:
                return
            if (node.left == None) and (node.right == None):
                min_depth = min(min_depth, depth)
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        min_depth = math.inf
        dfs(root, 1)
        return min_depth
        