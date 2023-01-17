class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans,ones=0,0
        for i in s:
            if i=='1':
                ones+=1
            elif ones>0:
                ans+=1
                ones-=1
        return ans