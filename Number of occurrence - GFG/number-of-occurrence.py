#User function Template for python3
from collections import Counter
class Solution:
    def binary(self,nums,target,leftbias):
        left,right=0,len(nums)-1
        i=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                i=mid
                if leftbias:
                    right=mid-1
                else:
                    left=mid+1
        return i
	def count(self,arr, n, x):
		left=self.binary(arr,x,True)
		right=self.binary(arr,x,False)
		return right-left+1 if x in arr else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends