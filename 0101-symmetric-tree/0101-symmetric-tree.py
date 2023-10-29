# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_symmetric(p, q):
            if not (p or q):
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return is_symmetric(p.left, q.right) and is_symmetric(p.right, q.left)

        return is_symmetric(root.left, root.right)
