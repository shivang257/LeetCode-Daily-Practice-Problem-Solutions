
class Solution(object):
    def isSubtree(self, r, s):
        if not s:
            return True
        if not r:
            return False
        
        if self.same(r,s):
            return True
        return self.isSubtree(r.left,s) or self.isSubtree(r.right,s)
    
    def same(self,r,s):
        if not s and not r:
            return True
        
        if r and s and r.val==s.val:
            return self.same(r.left,s.left) and self.same(r.right,s.right)
        
        else:
            return False