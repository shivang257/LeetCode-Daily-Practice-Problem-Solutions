# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        level=[root]
        while level and root:
            current=[]
            nextlevel=[]
            for i in level:
                current.append(i.val)
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            ans.append(current)
            level=nextlevel
        return ans