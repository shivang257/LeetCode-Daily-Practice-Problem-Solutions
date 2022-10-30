class Solution:
    def check(self,n,target):
            s=0
            while(n):
                s+=(n%10)
                n//=10
            return s<=target
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        s,x=0,10
        while (True):
            if self.check(n,target):
                return s
            else:
                t=x-(n%x)
                n+=t
                s+=t
                x*=10
        return s