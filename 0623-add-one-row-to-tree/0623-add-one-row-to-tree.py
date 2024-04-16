class Solution(object):
    def addOneRow(self, root, v, d):
        if d == 1:
            return TreeNode(v, root, None)
        
        bfs = deque([root])
        while bfs and d != 1:
            size = len(bfs)
            d -= 1
            for _ in range(size):
                curr = bfs.popleft()
                if curr.left != None:
                    bfs.append(curr.left)
                if curr.right != None:
                    bfs.append(curr.right)
                
                if d == 1: # Current level is in depth d-1 -> Add nodes with value `v`
                    curr.left = TreeNode(v, curr.left, None)
                    curr.right = TreeNode(v, None, curr.right)
        return root