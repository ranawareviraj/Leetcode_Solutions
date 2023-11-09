# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        # 1 -> 
        # head = 1

        # Preserve next node of the current node
        # next_node = 2
        # 1 -> X
        next_node = head.next
        head.next = None

        # Assume reverseList function returns head reversed LL starting next node
        # 2 <- 3 <- 4
        # new_head = 4
        new_head = self.reverseList(next_node)

        # Set the next node of the preseved node to the prev_head 
        # X <- 1 <- 2 <- 3 <- 4
        next_node.next = head
        return new_head
