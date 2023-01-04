class Solution:
    def smallestSubWithSum(self, a, n, x):
        curr,j,ans=0,0,10**100
        for i in range(n):
            curr+=a[i]
            if curr>x:
                ans=min(ans,i-j+1)
                while curr-a[j]>x:
                    curr-=a[j]
                    j+=1
                    ans=min(ans,i-j+1)
        return ans
                    
        
        
        
#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends