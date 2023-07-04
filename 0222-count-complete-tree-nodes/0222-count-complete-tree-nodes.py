class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        queue=deque()
        queue.append(root)
        if not root:
            return 0
        count=0
        while queue:
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                count+=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return count