#User function Template for python3
import collections
class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        d=collections.defaultdict(int)
        d[0]=-1
        pref=0
        ans=0
        for i in range(n):
            pref+=arr[i]
            
            if pref==k:
                ans=max(ans,i+1)
            if pref not in d:
                d[pref]=i
            if pref-k in d:
                ans=max(ans,i-d[pref-k])
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends