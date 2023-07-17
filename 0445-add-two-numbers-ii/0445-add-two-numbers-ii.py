class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1, st2 = [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next
            
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        
        carry, head = 0, None

        while st1 or st2 or carry:
            d1, d2 = 0, 0
            d1 = st1.pop() if st1 else 0
            d2 = st2.pop() if st2 else 0
            carry, digit = divmod(d1 + d2 + carry, 10)
            head_new = ListNode(digit)
            head_new.next = head
            head = head_new
              
        return head