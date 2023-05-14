class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        pCount,sCount=Counter(p),Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCount[s[i]]+=1
            if pCount==sCount:
                res.append(i-len(p)+1)
            sCount[s[i-len(p)+1]]-=1
            if sCount[s[i-len(p)+1]] == 0:
                del sCount[s[i-len(p)+1]]
        return res