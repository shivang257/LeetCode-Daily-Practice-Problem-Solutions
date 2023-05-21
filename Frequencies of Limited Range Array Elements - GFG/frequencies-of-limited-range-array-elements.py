import collections
class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        l=[i for i in range(1,N+1)]
        a=collections.Counter(arr)
        for i in range(N):
            arr[i]=a[l[i]]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends