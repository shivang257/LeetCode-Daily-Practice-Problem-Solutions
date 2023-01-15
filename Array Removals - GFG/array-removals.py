#User function Template for python3


class Solution:

	def removals(self,arr, n, k):
		# code here
		arr.sort()
		ans=-10**9
		for i in range(n):
		    for j in range(n):
		        if arr[j]-arr[i]<=k:
		            ans=max(ans,j-i+1)
		return n-ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.removals(arr, n, k)
        print(ans)
        tc -= 1
# } Driver Code Ends