class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        slow,fast=head,head.next
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        temp=slow.next
        slow.next=None
        root=TreeNode(temp.val)
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(temp.next)
        return root