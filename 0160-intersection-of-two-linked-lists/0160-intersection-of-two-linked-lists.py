class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1,p2=headA,headB
        while p1!=p2:
            if not p1:
                p1=headB
            else:
                p1=p1.next
            if not p2:
                p2=headA
            else:
                p2=p2.next
        return p1