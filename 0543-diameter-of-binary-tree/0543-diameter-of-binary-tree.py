# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def longest_path(node):
            if not node:
                return 0, 0  # Returning two values: diameter and depth

            left_diameter, left_depth = longest_path(node.left)
            right_diameter, right_depth = longest_path(node.right)

            # Diameter is the maximum of: current max diameter, left subtree diameter, right subtree diameter
            diameter = max(left_diameter, right_diameter, left_depth + right_depth)

            # Depth is the maximum depth of the current node
            depth = 1 + max(left_depth, right_depth)

            return diameter, depth

        diameter, _ = longest_path(root)
        return diameter
