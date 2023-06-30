class Solution:
    def check(self,p,q):
        if not p or not q:
            return not p and not q
        return p.val==q.val and self.check(p.left,q.right) and self.check(p.right,q.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.check(root.left,root.right)