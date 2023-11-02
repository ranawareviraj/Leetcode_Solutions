# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_good_nodes(node, max_so_far):
            if not node:
                return 0

            good_nodes_count = node.val >= max_so_far
            max_so_far = max(max_so_far, node.val)

            good_nodes_count += count_good_nodes(node.left, max_so_far)
            good_nodes_count += count_good_nodes(node.right, max_so_far)

            return good_nodes_count

        return count_good_nodes(root, root.val)