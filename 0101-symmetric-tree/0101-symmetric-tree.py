# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque()
        # Start comparison from roots left and right child
        queue.append(root.left)
        queue.append(root.right)

        while(queue):
            sub_tree1 = queue.popleft()
            sub_tree2 = queue.popleft()
            
            # If both the current nodes are null, continue validating next set of nodes
            if (not sub_tree1) and (not sub_tree2):
                continue

            # If either of the node is null, tree is not symmetric
            if (not sub_tree1) or (not sub_tree2):
                return False
            
            # If values of both the current nodes is not same, tree is not symmetric 
            if sub_tree1.val != sub_tree2.val:
                return False
                
            # Add nodes of both subtrees from opposite sides
            queue.append(sub_tree1.left)
            queue.append(sub_tree2.right)
            queue.append(sub_tree1.right)
            queue.append(sub_tree2.left)

        # If we reached till end without validation failure, tree is symmetric 
        return True
    
# Notes:
# left child node = left sub-tree
# right child node = right sub-tree