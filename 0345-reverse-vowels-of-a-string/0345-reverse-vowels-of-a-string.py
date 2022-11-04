class Solution:
    def reverseVowels(self, s: str) -> str:
        left,right=0,len(s)-1
        s=list(s)
        v='AEIOUaeiou'
        while left<right:
            if s[left] in v and s[right] in v:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            elif s[left] not in v:
                left+=1
            else:
                right-=1
        return ''.join(s)