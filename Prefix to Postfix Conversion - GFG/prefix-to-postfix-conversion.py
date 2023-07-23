#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def preToPost(self, pre_exp):
        res=[]
        for i in pre_exp[::-1]:
            if i.isalpha():
                res.append(i)
            else:
                a=res.pop()
                b=res.pop()
                res.append(a+b+i)
        return res[0]
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        prefix = input()
        ob = Solution()
        res = ob.preToPost(prefix)
        print(res)
# } Driver Code Ends