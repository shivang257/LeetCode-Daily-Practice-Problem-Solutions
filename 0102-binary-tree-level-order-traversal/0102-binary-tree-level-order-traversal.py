
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([root])
        res=[]
        if not root:
            return []
        while queue:
            cur=[]
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur.append(node.val)
            res.append(cur)
        return res