from collections import deque
class Solution:
   
   def KDistanceNodes(self,root,target,k):
       q = deque()
       q.append(root)
       x = None
       parent = dict()
       while len(q)>0:
           curr = q.popleft()
           if curr.data == target:
               x = curr
           if curr.left != None:
               q.append(curr.left)
               parent[curr.left] = curr
           if curr.right != None:
               q.append(curr.right)
               parent[curr.right] = curr
       if x == None:
           return []
       del q
       q = deque()
       q.append(x)
       visited = dict()
       visited[x] = True
       dist = 0
       while len(q)>0:
           if k == dist:
               break
           dist += 1
           y = len(q)
           for i in range(y):
               node = q.popleft()
               if node in parent and parent[node] not in visited:
                   q.append(parent[node])
                   visited[parent[node]] = True
               if node.left != None and node.left not in visited:
                   q.append(node.left)
                   visited[node.left] = True
               if node.right != None and node.right not in visited:
                   q.append(node.right)
                   visited[node.right] = True
       ans = []
       while len(q)>0:
           curr = q.popleft()
           ans.append(curr.data)
       ans.sort()
       return ans
 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

if __name__ == "__main__":
    x = Solution()
    t = int(input())
    for _ in range(t):
        line = input()
        target=int(input())
        k=int(input())

        root = buildTree(line)
        res = x.KDistanceNodes(root,target,k)
        
        for i in res:
            print(i, end=' ')
        print()

# } Driver Code Ends