class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n=len(s)
        l=[i for i in s]
        for i in range(n):
            l[i]=min(s[i],s[n-1-i])
            l[n-1-i]=l[i]
        return ''.join(l)