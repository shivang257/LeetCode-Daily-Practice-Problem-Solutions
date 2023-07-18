#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from collections import defaultdict
class Solution:
    def characterReplacement(self, s,k):
        freq=defaultdict(int)
        l,ans=0,0
        for r in range(len(s)):
            freq[s[r]]+=1
            if r-l+1-max(freq.values())<=k:
                ans=max(ans,r-l+1)
            else:
                freq[s[l]]-=1
                l+=1
        return ans
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range(t):
        S = input().strip()
        K = int(input())
        ob = Solution()
        res = ob.characterReplacement(S, K)
        print(res)
# } Driver Code Ends