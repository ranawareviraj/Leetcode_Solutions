# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build_tree(left, right):
            nonlocal postorder_index
            if left > right:
                return None
            
            val = postorder[postorder_index]
            node = TreeNode(val)
            postorder_index -= 1
            pivot_index = index_map[ val ]
            node.right = build_tree(pivot_index + 1, right)
            node.left = build_tree(left, pivot_index - 1)

            return node

        index_map = {}
        for index, val in enumerate(inorder):
            index_map[ val ] = index

        n = len(inorder)
        postorder_index = n - 1        
        return build_tree(0, n - 1)