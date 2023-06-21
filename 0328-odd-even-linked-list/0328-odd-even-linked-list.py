class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d1=odd=ListNode(0)
        d2=even=ListNode(0)
        i=1
        while head:
            odd.next=head
            even.next=head.next
            odd=odd.next
            even=even.next
            head=head.next.next if even else None
        odd.next=d2.next
        return d1.next