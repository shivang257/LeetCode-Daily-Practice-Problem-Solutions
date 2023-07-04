class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            ino=inorder.index(preorder.pop(0))
            root=TreeNode(inorder[ino])
            root.left=self.buildTree(preorder,inorder[:ino])
            root.right=self.buildTree(preorder,inorder[ino+1:])
            return root