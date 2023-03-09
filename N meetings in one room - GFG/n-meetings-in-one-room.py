#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meetings=[(start[i],end[i]) for i in range(len(end))]
        meetings.sort()
        ans,curr=0,[0,0]
        for i in range(len(end)):
            if curr[0]<=meetings[i][1] and curr[1]>=meetings[i][0]:
                if meetings[i][1]<curr[1]:
                    curr=meetings[i]
            else:
                ans+=1
                curr=meetings[i]
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends