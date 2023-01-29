# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            height=1+max(left,right)
            self.res=max(self.res,left+right)
            return height
        dfs(root)
        return self.res