# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal min_diff
            nonlocal prev

            if not node:
                return
            
            # visit left subtree
            dfs(node.left)

            # visit root
            if prev:
                min_diff = min(min_diff, node.val - prev.val)
            prev = node
            
            # visit right subtree
            dfs(node.right)

        min_diff = math.inf
        prev = None
        dfs(root)
        return min_diff
