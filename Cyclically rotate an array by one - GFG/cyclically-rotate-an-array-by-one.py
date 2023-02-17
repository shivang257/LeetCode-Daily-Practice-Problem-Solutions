#User function Template for python3

def rotate( arr, n):
    left,right=0,n-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
    return arr
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends