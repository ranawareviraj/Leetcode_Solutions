# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has_path_sum(node, curr_sum, target_sum):
            if not node:
                return False

            curr_sum += node.val

            if not (node.left or node.right):
                return (curr_sum == targetSum)
            
            path_sum_in_left = has_path_sum(node.left, curr_sum, target_sum)
            path_sum_in_right = has_path_sum(node.right,  curr_sum, target_sum)

            return path_sum_in_left or path_sum_in_right
        
        return has_path_sum(root, 0, targetSum)