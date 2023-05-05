class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ans,j=0,0
        unique=1
        for i in range(1,len(word)):
            if word[i-1]>word[i]:
                j=i
                unique=1
            elif word[i-1]<word[i]:
                unique+=1
            if unique==5:
                ans=max(ans,i-j+1)
        return ans