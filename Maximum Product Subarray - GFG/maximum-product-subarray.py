#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,nums, n):
		a=nums[::-1]
		for i in range(1,n):
		    a[i]*=a[i-1] or 1
		    nums[i]*=nums[i-1] or 1
		return max(a+nums)


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends