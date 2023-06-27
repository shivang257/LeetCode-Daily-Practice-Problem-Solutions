class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def height(root):
            if not root:
                return 0
            left,right=height(root.left),height(root.right)
            self.ans=max(self.ans,left+right)
            return 1+max(left,right)
        height(root)
        return self.ans