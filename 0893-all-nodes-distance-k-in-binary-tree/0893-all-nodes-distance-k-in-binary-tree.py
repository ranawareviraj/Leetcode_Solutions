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
        
        parents = {}
        dfs(root, None)

        queue = deque([ target ])
        level = 0
        seen = set([target])

        while queue and level < k:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()

                for neighbor in [node.left, node.right, parents[node]]:
                    if neighbor and neighbor not in seen:
                        queue.append(neighbor)
                        seen.add(neighbor)

            level += 1
        
        result = []
        for node in queue:
            result.append(node.val)
        
        return result

