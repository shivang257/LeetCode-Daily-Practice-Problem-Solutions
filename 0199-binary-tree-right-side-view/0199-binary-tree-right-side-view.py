class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=deque()
        res=[]
        if root:
            q.append(root)
        while q:
            rightside=None
            n=len(q)
            for i in range(n):
                node=q.popleft()
                if node:
                    rightside=node
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                res.append(rightside.val)
        return res