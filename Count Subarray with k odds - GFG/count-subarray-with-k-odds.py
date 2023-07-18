#User function Template for python3

class Solution:
    def countSubarray(self, n, nums, k):
        count,res=0,0
        l=0
        for r in range(n):
            if nums[r]%2:
                k-=1
                count=0
            while k==0:
                k+=nums[l]%2
                l+=1
                count+=1
            res+=count
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        print(ob.countSubarray(n, nums, k))
# } Driver Code Ends