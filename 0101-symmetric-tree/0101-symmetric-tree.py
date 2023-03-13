# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def issym(l,r):
            if not l and not r:
                return True
            if l and r and l.val==r.val:
                return issym(l.left,r.right) and issym(l.right,r.left)
            return False
        return issym(root,root)