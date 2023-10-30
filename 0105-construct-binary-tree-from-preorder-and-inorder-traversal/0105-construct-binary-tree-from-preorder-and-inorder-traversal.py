# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build_tree(preorder, inorder, index_map):
            if not preorder or not inorder:
                return None
            
            # First node in preorder traversal is root node. 
            # Find its index in inorder traversal list - total nodes in left subtree
            node = TreeNode(preorder[0])
            pivot = inorder.index(preorder[0])

            # Send left subtree elements to the left of current node and
            # Send right subtree elements to the right of current node
            node.left = build_tree(preorder[1 : pivot + 1], inorder[ : pivot], index_map)
            node.right = build_tree(preorder[pivot + 1 : ], inorder[pivot + 1 : ], index_map)
            
            return node
         
        # Build index map for nodes in inorder traversal list for constant time lookup
        index_map = {}
        for node, index in enumerate(inorder):
            index_map[node] = index
        
        return build_tree(preorder, inorder, index_map)
