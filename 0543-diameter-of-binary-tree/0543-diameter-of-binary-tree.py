class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        
        def dfs(root):
            if not root:
                return 0
            
            left=dfs(root.left)
            right=dfs(root.right)
            height=max(left,right)+1
            self.res=max(self.res,left+right)
            
            return height
        dfs(root)
        
        return self.res