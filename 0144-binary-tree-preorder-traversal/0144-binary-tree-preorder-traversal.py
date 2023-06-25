class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def post(root):
            if root:
                res.append(root.val)
                post(root.left)
                post(root.right)
        post(root)
        return res