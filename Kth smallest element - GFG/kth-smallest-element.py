#User function Template for python3

class Solution:
    def kthSmallest(self,arr, l, r, k):
        m={}
        for i in arr:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        freq=0
        for i in sorted(m.keys()):
            freq+=m[i]
            if freq>=k:
                return i

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends