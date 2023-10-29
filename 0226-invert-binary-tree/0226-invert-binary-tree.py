# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        
        # If root is not null, push it onto queue
        if root:
            queue.append(root)
        
        while queue:
            # Pop the node
            node = queue.popleft()

            # Perform inversion
            node.left, node.right =  node.right, node.left

            # Add next level onto queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root