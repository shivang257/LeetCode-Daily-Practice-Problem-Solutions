# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast,slow,entry=head,head,head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                while slow!=entry:
                    slow=slow.next
                    entry=entry.next
                return slow
        return None