class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:
                return 0
            return 1+max(height(root.left),height(root.right))
        return height(root)