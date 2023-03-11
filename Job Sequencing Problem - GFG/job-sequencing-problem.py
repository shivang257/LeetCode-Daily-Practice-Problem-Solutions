#User function Template for python3

class Solution:
    def JobScheduling(self,jobs,n):
        jobs.sort(key=lambda x:x.profit,reverse=True)
        vis=[0]*(n)
        ans,count=0,0
        for i in range(n):
            for j in range(jobs[i].deadline-1,-1,-1):
                if vis[j]:
                    continue
                else:
                    vis[j]=True
                    count+=1
                    ans+=jobs[i].profit
                    break
        return (count,ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends