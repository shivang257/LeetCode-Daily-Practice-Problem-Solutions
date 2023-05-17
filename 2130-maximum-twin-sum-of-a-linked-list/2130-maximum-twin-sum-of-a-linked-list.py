class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        maxVal = 0

        # Get middle of linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second part of linked list
        curr, prev = slow, None

        while curr:       
            curr.next, prev, curr = prev, curr, curr.next   

        # Get max sum of pairs
        while prev:
            maxVal = max(maxVal, head.val + prev.val)
            prev = prev.next
            head = head.next

        return maxVal