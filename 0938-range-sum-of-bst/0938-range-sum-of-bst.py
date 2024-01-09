# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], L: int, R: int) -> int:
        # Base case
        if not root:
            return 0

        if R < root.val:
            return self.rangeSumBST(root.left, L, R)
        if L > root.val:
            return self.rangeSumBST(root.right, L, R)

        return (root.val
                + self.rangeSumBST(root.left, L, R) 
                + self.rangeSumBST(root.right, L, R))
