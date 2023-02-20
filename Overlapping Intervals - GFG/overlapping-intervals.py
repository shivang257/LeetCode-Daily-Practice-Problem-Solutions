class Solution:
	def overlappedInterval(self, intervals):
		#Code here
		intervals.sort()
		output=[intervals[0]]
		for start,end in intervals[1:]:
		    last=output[-1][1]
		    if last>=start:
		        output[-1][1]=max(last,end)
		    else:
		        output.append([start,end])
		return output


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends