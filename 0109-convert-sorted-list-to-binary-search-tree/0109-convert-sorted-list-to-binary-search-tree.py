# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def find_mid(node):
            prev = None
            fast = slow = node
            while (fast) and (fast.next):
                fast = fast.next.next
                prev = slow
                slow = slow.next
            
            # If LL has at least two node, break list from mid point
            # i.e set next of prev -> mid as None
            if prev:
                prev.next = None
            return slow
        
        # If LL is empty, return null
        if not head:
            return None

        mid = find_mid(head)
        node = TreeNode(mid.val)

        # If LL mid is head itself, then its leaft node. Return it
        if head == mid:
            return node
        
        # Recursively build left and right subtrees
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)

        return node