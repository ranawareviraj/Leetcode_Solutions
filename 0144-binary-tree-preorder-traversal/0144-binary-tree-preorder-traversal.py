# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, result):
            if node:
                result.append(node.val)
                dfs(node.left, result)
                dfs(node.right, result)
        
        result = []
        dfs(root, result)
        return result
    