class Solution:
    def removeNodes(self, head):
        if not head: return None
        head.next = self.removeNodes(head.next)
        if head.next and head.val < head.next.val:
            return head.next
        return head