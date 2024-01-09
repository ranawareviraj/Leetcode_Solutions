# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(root):
            stack = [root]
            sequence = []
            while stack:
                node = stack.pop()

                if not node.left and not node.right:
                    sequence.append(node.val)

                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

            return sequence

        return helper(root1) == helper(root2) 
    