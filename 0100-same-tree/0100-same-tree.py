# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both trees are Null, they are same tree
        if not p and not q:
            return True
        
        # Else if either of the tree is Null, they are not same tree
        if not p or not q:
            return False
        
        # Else values of respective nodes aren't same, they are not same tree
        if p.val != q.val:
            return False
        
        # For trees to be same, the left and right subtrees must be same
        is_same_tree_left = self.isSameTree(p.left, q.left)
        is_same_tree_right = self.isSameTree(p.right, q.right)

        return is_same_tree_left and is_same_tree_right