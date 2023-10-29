# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0

        def find_all_path_sum(node, path):
            nonlocal result
            if not node:
                return
            
            if not (node.left or node.right):
                result += int("".join(path[:] + [str(node.val)]))

            find_all_path_sum(node.left, path[:] + [str(node.val)])
            find_all_path_sum(node.right, path[:] + [str(node.val)])
        
        find_all_path_sum(root, [])
        return result