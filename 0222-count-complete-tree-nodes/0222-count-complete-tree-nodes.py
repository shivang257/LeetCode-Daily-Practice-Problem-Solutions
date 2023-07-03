class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count=0
        queue=deque()
        queue.append(root)
        if not root:
            return 0
        while queue:
            size=len(queue)
            temp=[]
            for i in range(size):
                node=queue.popleft()
                temp.append(node.val)
                count+=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return count