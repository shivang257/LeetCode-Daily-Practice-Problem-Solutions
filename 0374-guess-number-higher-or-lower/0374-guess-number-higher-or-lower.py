class Solution:
    def guessNumber(self, n: int) -> int:
        md=n//2
        l=0
        r=n
        x=guess(md)
        while(x!=0 and l<r):
            print(md)
            if(x==1):
                l=md+1
                md=(l+r)//2
                x=guess(md)
            else:
                r=md-1
                md=(l+r)//2
                x=guess(md)
        return md