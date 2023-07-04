class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(root,val):
            if root and root.val<val:
                return dfs(root.right,val)
            elif root and root.val>val:
                return dfs(root.left,val)
            return root
        return dfs(root,val)