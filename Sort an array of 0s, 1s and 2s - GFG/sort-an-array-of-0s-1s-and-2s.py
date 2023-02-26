#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        start,mid,end=0,0,n-1
        while mid<=end:
            if arr[mid]==0:
                arr[start],arr[mid]=arr[mid],arr[start]
                mid+=1
                start+=1
            elif arr[mid]==2:
                arr[end],arr[mid]=arr[mid],arr[end]
                end-=1
            else:
                mid+=1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends