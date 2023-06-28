class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res,level,flag=[],[root],1
        while level and root:
            current=[]
            nextlevel=[]
            for node in level:
                current.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            res+=[current[::flag]]
            level=nextlevel
            flag*=-1
        return res