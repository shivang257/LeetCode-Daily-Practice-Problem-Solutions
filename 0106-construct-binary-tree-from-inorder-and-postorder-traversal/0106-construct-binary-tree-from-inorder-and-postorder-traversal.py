class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root=TreeNode(postorder.pop())
        ino=inorder.index(root.val)
        root.right=self.buildTree(inorder[ino+1:],postorder)
        root.left=self.buildTree(inorder[:ino],postorder)
        return root