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
            top = top.next
            if top:
                heapq.heappush(heap, (top.val, id(top), top))
        
        return dummy.next

        
        