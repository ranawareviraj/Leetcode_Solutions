# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()
        if root:
            queue.append(root)

        to_reverse = False
        while queue:
            n = len(queue)
            level = []

            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if to_reverse:
                result.append(reversed(level))
            else:
                result.append(level)
            to_reverse = not to_reverse

        return result
        