#User function Template for python3


class Solution:
    def smallestSumSubarray(self, a, n):
        #Your code here
        m1,m2=10**9,10**9
        for i in range(n):
            m1=min(m1+a[i],a[i])
            m2=min(m1,m2)
        return m2


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.smallestSumSubarray(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends