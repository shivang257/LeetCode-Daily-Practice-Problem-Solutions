class Solution:
    def longestPalindrome(self, s: str) -> str:
        l,r=0,0
        n=len(s)
        res=""
        for i in range(n):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            tem=s[l+1:r]
            if len(tem)>len(res):
                res=tem
        for i in range(n):
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            tem=s[l+1:r]
            if len(tem)>len(res):
                res=tem
        return res