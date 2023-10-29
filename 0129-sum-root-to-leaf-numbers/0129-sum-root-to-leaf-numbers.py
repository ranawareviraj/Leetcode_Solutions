# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def find_all_path_sum(node, curr_number):
            nonlocal result
            if not node:
                return
            
            curr_number = curr_number * 10 + node.val
            if not (node.left or node.right):
                result += curr_number
            
            find_all_path_sum(node.left, curr_number)
            find_all_path_sum(node.right, curr_number)
            
        result = 0
        find_all_path_sum(root, 0)
        return result
        