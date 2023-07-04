#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        ans = 0
        pd = 1
        prev = 0
        for i in range(n):
            pd *= a[i]
            while pd >= k and prev <= i:
                pd /= a[prev]
                prev += 1
            ans += i - prev + 1
        return ans
    

#{ 
 # Driver Code Starts

#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends