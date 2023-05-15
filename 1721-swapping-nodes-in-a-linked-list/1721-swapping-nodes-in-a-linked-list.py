class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        slow, fast = head, head
        for _ in range(k - 1):
            fast = fast.next
        first = fast
        while fast.next:
            slow, fast = slow.next, fast.next
        first.val, slow.val = slow.val, first.val
        return head