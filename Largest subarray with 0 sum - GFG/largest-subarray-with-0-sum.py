#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        d={0:1}
        ans=0
        pref=0
        for i in range(n):
            pref+=arr[i]
            if pref==0:
                ans=i+1
            if pref not in d:
                d[pref]=i
            if pref in d:
                ans=max(ans,i-d[pref])
        return ans
        


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends