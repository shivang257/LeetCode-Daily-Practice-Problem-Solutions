class Solution(object):
    def sumNumbers1(self, root): # DFS recursively 
        self.res = 0
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, root, path):
        if root:
            if not root.left and not root.right:
                path = path*10 + root.val
                self.res += path
            self.dfs(root.left, path*10+root.val)
            self.dfs(root.right, path*10+root.val)
            
    def sumNumbers2(self, root): # BFS with queue
        deque, res = collections.deque(), 0
        if root:
            deque.append(root)
        while deque:
            node = deque.popleft()
            if not node.left and not node.right:
                res += node.val
            if node.left:
                node.left.val += node.val*10
                deque.append(node.left)
            if node.right:
                node.right.val += node.val*10
                deque.append(node.right)
        return res
    
    def sumNumbers(self, root): # DFS with stack
        stack, res = [], 0
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                res += node.val
            if node.right:
                node.right.val += node.val*10
                stack.append(node.right)
            if node.left:
                node.left.val += node.val*10
                stack.append(node.left)
        return res