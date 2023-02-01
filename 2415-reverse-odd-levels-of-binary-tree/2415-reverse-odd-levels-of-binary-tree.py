# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root1,root2,l):
        if not root1 and not root2:
            return
        if l%2==1:
            root1.val,root2.val=root2.val,root1.val
        self.solve(root1.left,root2.right,l+1)
        self.solve(root1.right,root2.left,l+1)
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.solve(root.left,root.right,1)
        return root