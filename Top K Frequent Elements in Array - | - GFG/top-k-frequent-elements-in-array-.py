import collections
class Solution:
	def topK(self, nums, k):
		#Code here
		l=[]
		nums.sort(reverse=True)
		a=collections.Counter(nums).most_common()
		a=sorted(a,key=lambda x:x[0],reverse=True)
		a=sorted(a,key=lambda x:x[1],reverse=True)
		for i in range(k):
		    l.append(a[i][0])
		return l

#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
# } Driver Code Ends