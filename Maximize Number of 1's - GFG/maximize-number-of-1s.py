def findZeroes(nums, n, k) :
    zeros=0
    left,right=0,0
    m=0
    for right in range(n):
        if nums[right]==0:
            zeros+=1
        right+=1
        if zeros>k:
            if nums[left]==0:
                zeros-=1
            left+=1
        m=max(m,right-left)
    return m
#{ 
 # Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        m=int(input())
        ans= findZeroes(arr, n, m)
        print(ans)
        tc=tc-1
# } Driver Code Ends