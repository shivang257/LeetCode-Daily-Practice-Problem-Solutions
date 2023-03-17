#User function Template for python3
class Solution:
    def dfs(self,i,num,sum,ans):
        if i==len(num):
            ans.append(sum)
            return
        self.dfs(i+1,num,sum+num[i],ans)
        self.dfs(i+1,num,sum,ans)
	def subsetSums(self, arr, N):
		# code here
		sum=0
		ans=[]
		self.dfs(0,arr,0,ans)
		return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends