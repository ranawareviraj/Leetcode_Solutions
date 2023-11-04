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

        nodes = defaultdict(Node)
        new_root = Node(node.val, [])
        nodes[node.val] = new_root

        seen = set()
        stack = [ node ]
  
        while stack:
            old_node = stack.pop()

            for neighbor in old_node.neighbors:
                if neighbor.val not in nodes:
                    nodes[neighbor.val] = Node(neighbor.val, [])
                    stack.append( neighbor )
                
                current_node = nodes[old_node.val]
                current_neighbor = nodes[neighbor.val]
                
                current_node.neighbors.append(current_neighbor)
                
        return nodes[node.val]