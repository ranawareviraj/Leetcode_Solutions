# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def find_paths(node, p, q, path):
            nonlocal paths
            if node:
                new_path = path[:] + [node]
                if node.val == p.val or node.val == q.val:
                    paths.append(new_path)
                
                find_paths(node.left, p, q, new_path)
                find_paths(node.right, p, q, new_path)
        
        # Find paths from root to node p and q
        paths = []
        find_paths(root, p, q, [])
        
        # Find the first node after which their paths diverge
        n = min(len(paths[0]), len(paths[1]))
        prev = root
        for i in range(n):
            if paths[0][i].val != paths[1][i].val:
                return prev
            prev = paths[0][i] # or paths[1][i]
        
        return prev
