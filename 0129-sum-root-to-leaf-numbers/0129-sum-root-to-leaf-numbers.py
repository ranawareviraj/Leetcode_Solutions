# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def find_all_path_sum(node, curr_sum):
            if not node:
                return 0
            
            curr_sum = curr_sum * 10 + node.val
            if not (node.left or node.right):
                return curr_sum
            
            left_sum = find_all_path_sum(node.left, curr_sum)
            right_sum = find_all_path_sum(node.right, curr_sum)

            return left_sum + right_sum
        
        return find_all_path_sum(root, 0)
