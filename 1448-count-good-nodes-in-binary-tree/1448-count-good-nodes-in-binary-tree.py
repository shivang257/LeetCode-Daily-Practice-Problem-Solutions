class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root,m):
            if not root:
                return 0
            if root.val>=m:
                res=1
            else:
                res=0
            m=max(m,root.val)
            res+=dfs(root.left,m)
            res+=dfs(root.right,m)
            return res
        return dfs(root,root.val)