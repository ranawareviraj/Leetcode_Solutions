# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        n = len(postorder)
        node = TreeNode(postorder[-1])
        pivot = inorder.index(postorder[-1])

        node.left = self.buildTree(inorder[: pivot], postorder[0: pivot])
        node.right = self.buildTree(inorder[pivot + 1 : ], postorder[pivot: n - 1])

        return node