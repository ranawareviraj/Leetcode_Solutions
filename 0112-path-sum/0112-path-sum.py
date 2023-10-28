# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not (root.left or root.right):
            return (root.val == targetSum)
        
        path_sum_in_left = self.hasPathSum(root.left, targetSum - root.val)
        path_sum_in_right = self.hasPathSum(root.right, targetSum - root.val)

        return path_sum_in_left or path_sum_in_right