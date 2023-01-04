#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        mi=arr[0]
        mx=arr[n-1]
        minh=mx-mi
        for i in range(1,n):
            if k>arr[i]:
                continue
            mi=min(arr[0]+k,arr[i]-k)
            mx=max(arr[n-1]-k,arr[i-1]+k)
            minh=min(minh,mx-mi)
        return minh

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends