class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(root,val):
            if not root:
                return None
            if root.val==val:
                return root
            elif root.val>val:
                return dfs(root.left,val)
            else:
                return dfs(root.right,val)
        return dfs(root,val)