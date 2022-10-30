class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def c(n,target):
            s=0
            while(n):
                s+=(n%10)
                n//=10
            return s<=target
        s=0
        x=10
        while (True):
            if c(n,target):
                return s
            else:
                t=x-(n%x)
                n+=t
                s+=t
                x*=10
        return s