# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        fast,slow,entry=head,head,head
        while fast.next is not None and fast.next.next is not None:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                while entry!=slow:
                    entry=entry.next
                    slow=slow.next
                return slow
        return None