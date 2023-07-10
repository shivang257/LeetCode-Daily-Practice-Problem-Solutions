class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue=deque()
        queue.append([root,1])
        if not root:
            return 0
        while queue:
            node,level=queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append([node.left,level+1])
                    queue.append([node.right,level+1])
        