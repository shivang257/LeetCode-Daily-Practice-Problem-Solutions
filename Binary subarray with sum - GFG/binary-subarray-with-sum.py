#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, arr, N, target):
        mp=defaultdict(int)
        mp[0]=1
        psum=0
        res=0
        for i in arr:
            psum+=i
            res+=mp[psum-target]
            mp[psum]+=1
        return res
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, target = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.numberOfSubarrays(arr, N, target)
        print(res)
# } Driver Code Ends