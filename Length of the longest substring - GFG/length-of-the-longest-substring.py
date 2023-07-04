#User function Template for python3

class Solution:
    def longestUniqueSubsttr(self, S):
        left,output,seen=0,0,{}
        for right,curr in enumerate(s):
            if curr in seen:
                left=max(left,seen[curr]+1)
            output=max(output,right-left+1)
            seen[curr]=right
        return output

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        
        
        ob=Solution()
        print(ob.longestUniqueSubsttr(s))
# } Driver Code Ends