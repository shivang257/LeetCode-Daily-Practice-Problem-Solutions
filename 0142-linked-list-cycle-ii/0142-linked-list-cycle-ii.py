class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=set()
        while head:
            if head in s:
                return head
            s.add(head)
            head=head.next
        return None