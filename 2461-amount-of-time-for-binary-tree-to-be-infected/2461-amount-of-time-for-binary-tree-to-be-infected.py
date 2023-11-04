# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import *

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # DFS to build a node to parent map
        def dfs(node, parent):
            nonlocal start_node
            if not node:
                return
            
            if not start_node and node.val == start:
                start_node = node

            if node and parent:
                parents[node.val] = parent

            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)
        
        # Neighbors of a node are - node.left, node.right and parent
        # Build node to parent map
        start_node = None
        parents = {}
        dfs(root, None)

        # Perform BFS staring target node
        queue = deque([start_node])
        time_elapsed = -1
        seen = { start_node }

        while queue:
            # size of the current level
            l = len(queue)

            # Process current level
            for _ in range(l):
                node = queue.popleft()
            
                # Add next level onto queue
                for neighbor in [node.left, node.right, parents.get(node.val, None)]:
                    if neighbor and neighbor not in seen:
                        queue.append(neighbor)
                        seen.add(neighbor)

            time_elapsed += 1

        return time_elapsed
    