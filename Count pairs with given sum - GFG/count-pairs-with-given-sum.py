#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        c=0
        m={}
        for i in range(n):
            target=k-arr[i]
            if target in m:
                c+=m[target]
            if arr[i] in m:
                m[arr[i]]+=1
            else:
                m[arr[i]]=1
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends