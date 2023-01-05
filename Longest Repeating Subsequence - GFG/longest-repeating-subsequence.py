#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, str):
		a=str
		dp=[[0]*(len(a)+1) for i in range(len(a)+1)]
		for i in range(len(a)):
		    for j in range(len(str)):
		        if a[i]==str[j] and i!=j:
		            dp[i+1][j+1]=dp[i][j]+1
		        else:
		            dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
		return dp[-1][-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

# } Driver Code Ends