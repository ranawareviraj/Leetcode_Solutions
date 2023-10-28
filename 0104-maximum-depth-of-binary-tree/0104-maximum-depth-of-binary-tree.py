# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        queue = deque()
        if root:
            queue.append((root, 1))
        
        while queue:
            node, level = queue.popleft()
            if not (node.left or node.right):
                max_depth = max(max_depth, level)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return max_depth