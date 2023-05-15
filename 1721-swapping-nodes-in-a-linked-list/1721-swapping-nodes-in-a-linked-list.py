class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        slow, fast = head, head
        
# move the fast pointer to kth node
        for _ in range(k - 1):
            fast = fast.next
        first = fast
        
# move the fast pointer to end of the linked list 
# then slow pointer will be at kth node from the end
        while fast.next:
            slow, fast = slow.next, fast.next
            
# swap the values
        first.val, slow.val = slow.val, first.val
        return head