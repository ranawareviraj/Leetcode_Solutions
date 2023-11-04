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
        queue = deque([ node ])
  
        while queue:
            old_node = queue.popleft()

            for neighbor in old_node.neighbors:
                if neighbor.val not in nodes:
                    new_neighbor = Node(neighbor.val, [])
                    nodes[neighbor.val] = new_neighbor
                    queue.append( neighbor )
                
                nodes[old_node.val].neighbors.append(nodes[neighbor.val])
                
        return nodes[node.val]