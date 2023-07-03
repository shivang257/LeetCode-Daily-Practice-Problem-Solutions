#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

from collections import deque
class Solution:
    def countNodes(self, root):
        queue=deque()
        queue.append(root)
        count=0
        if not root:
            return 0
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
        
        

#{ 
 # Driver Code Starts.
from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
def constructTree(idx, arr):
    if idx >= len(arr):
        return None
    root = Node(arr[idx])
    root.left = constructTree(2 * idx + 1, arr)
    root.right = constructTree(2 * idx + 2, arr)
    return root
        
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        v = list(map(int, input().split()))
        root = constructTree(0, v)
        obj = Solution()
        print(obj.countNodes(root))
# } Driver Code Ends