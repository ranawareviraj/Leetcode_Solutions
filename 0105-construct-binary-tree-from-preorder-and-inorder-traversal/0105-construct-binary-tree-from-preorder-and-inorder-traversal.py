# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build_tree(left, right):
            nonlocal preorder_index

            if left > right:
                return None
            
            node_val = preorder[preorder_index]
            node = TreeNode(node_val)

            pivot = index_map[node_val]
            preorder_index += 1

            # print(node_val)

            # Send left subtree elements to the left of current node and
            # Send right subtree elements to the right of current node
            node.left = build_tree(left, pivot - 1)
            node.right = build_tree(pivot + 1, right)
            
            return node

        index_map = {}
        for index, node in enumerate(inorder):
            index_map[ node ] = index

        preorder_index = 0
        return build_tree(0, len(inorder) - 1)
