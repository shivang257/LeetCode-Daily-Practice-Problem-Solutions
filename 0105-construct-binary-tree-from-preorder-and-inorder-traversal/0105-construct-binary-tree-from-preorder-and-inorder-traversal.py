# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, pre: List[int], inor: List[int]) -> Optional[TreeNode]:
        if not inor or not pre:
            return None
        root=TreeNode(pre[0])
        mid=inor.index(pre[0])
        root.left=self.buildTree(pre[1:mid+1],inor[:mid])
        root.right=self.buildTree(pre[mid+1:],inor[mid+1:])
        return root