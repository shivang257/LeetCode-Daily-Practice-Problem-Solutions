

class Solution:
    def buildtree(self, ino, pre, n):
        if n==0:
            return None
        root=Node(pre[0])
        mid=ino.index(pre[0])
        root.left=self.buildtree(ino[:mid],pre[1:mid+1],mid)
        root.right=self.buildtree(ino[mid+1:],pre[mid+1:],n-mid-1)
        return root

        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        inorder = [ int(x) for x in input().split() ]
        preorder = [ int(x) for x in input().split() ]
        
        root = Solution().buildtree(inorder, preorder, n)
        printPostorder(root)
        print()

# } Driver Code Ends