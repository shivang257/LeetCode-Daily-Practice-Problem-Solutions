class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        
        if p and q and p.val==q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
        else:
            return False