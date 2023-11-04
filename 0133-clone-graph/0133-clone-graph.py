from collections import defaultdict
from typing import Optional

# # Definition for a Node.
# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        def dfs(old_node):
            if old_node.val in nodes:
                return nodes[old_node.val]
            
            new_node = Node(old_node.val, [])
            nodes[old_node.val] = new_node

            for neighbor in old_node.neighbors:
                new_neighbor = dfs(neighbor)
                new_node.neighbors.append(new_neighbor)

            return new_node

        nodes = defaultdict(Node)
        return dfs(node)
