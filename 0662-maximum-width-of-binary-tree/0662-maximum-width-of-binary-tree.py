class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue=[(root,0)]
        ans=0
        while queue:
            ans=max(queue[-1][1]-queue[0][1]+1,ans)
            size=len(queue)
            temp=[]
            for node,i in queue:
                if node.left:
                    temp.append((node.left,2*i+1))
                if node.right:
                    temp.append((node.right,2*i+2))
            queue=temp
        return ans