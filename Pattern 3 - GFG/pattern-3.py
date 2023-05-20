#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i+1):
                print(j+1,end=" ")
            print()

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends