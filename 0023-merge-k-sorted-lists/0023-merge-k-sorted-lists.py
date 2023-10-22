# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, id(head), head))
       
        dummy = ListNode(-1)
        curr = dummy
        while heap:
            val, _, top = heapq.heappop(heap)
            curr.next = top
            curr = curr.next
            node = top.next
            if node:
                heapq.heappush(heap, (node.val, id(node), node))
        
        return dummy.next

        
        