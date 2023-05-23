#User function Template for python3


# m is maximum of number zeroes allowed 
# to flip, n is size of array 
def findZeroes(arr, n, k) :
    # code here
    left,right=0,0
    zeros=0
    m=0
    while right<len(arr):
        zeros+=1-arr[right]
        right+=1
        if zeros>k:
            zeros-=1-arr[left]
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