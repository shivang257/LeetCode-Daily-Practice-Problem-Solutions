class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res,level=[],[root]
        flag=1
        while level and root:
            current=[]
            nextLevel=[]
            for node in level:
                current.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            res+=[current[::flag]]
            level=nextLevel
            flag*=-1
        return res