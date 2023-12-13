# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def dfs_inorder(node, p, successor):
            if not node:
                return successor

            if p.val >= node.val:
                return dfs_inorder(node.right, p, successor)
            
            return dfs_inorder(node.left, p, node)
        
        return dfs_inorder(root, p, None)
