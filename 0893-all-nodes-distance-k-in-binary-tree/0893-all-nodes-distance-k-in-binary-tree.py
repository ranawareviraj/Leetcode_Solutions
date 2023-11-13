# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent):
            if not node:
                return

            parents[node] = parent

            dfs(node.left, node)
            dfs(node.right, node)    
        
        # Use DFS (or BFS) to get parent of each node
        parents = {}
        dfs(root, None)

        # Start BFS from target node treating tree as undirected graph 
        # with parent, left_child and right_child as neighbors
        queue = deque([ target ])
        level = 0
        seen = set([target])

        # Using BFS traverse and find all nodes k distance away from the target node
        while queue and level < k:
            # Size of the current level
            n = len(queue)

            # Traverse current level
            for _ in range(n):
                node = queue.popleft()

                # Push next level onto queue
                neighbors = [ node.left, node.right, parents[node] ]
                for neighbor in neighbors:
                    if neighbor and neighbor not in seen:
                        queue.append(neighbor)
                        seen.add(neighbor)
            # Increment level
            level += 1
        
        # From queue, capture all nodes at the current (kth) level
        result = []
        for node in queue:
            result.append(node.val)
        
        return result
