# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: 
            return head
        return self.sort(head)

    def sort(self, head):
        def merge(left, right):
            dummy = ListNode(-1)
            curr = dummy

            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next

            curr.next = left if left else right

            return dummy.next
        
        def find_mid(head):
            prev = None
            fast = slow = head

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            if prev:
                prev.next = None
            return slow

        mid = find_mid(head)
        if head == mid:
            return head
            
        left = self.sort(head)
        right = self.sort(mid)

        return merge(left, right)
