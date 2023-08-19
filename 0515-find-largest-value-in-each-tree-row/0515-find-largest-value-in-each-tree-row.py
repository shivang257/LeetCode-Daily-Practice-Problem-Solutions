class Solution:
    def largestValues(self, root):
        if not root:
            return []
        res = [] 
        q = collections.deque([root])
        while q:
            res.append(max(x.val for x in q))
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return res 