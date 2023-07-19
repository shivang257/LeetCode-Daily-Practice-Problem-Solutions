class Solution:
    def maxScore(self, c: List[int], k: int) -> int:
        i=0
        s=0
        size=len(c)-k
        mins=float('inf')
        for j in range(len(c)):
            s+=c[j]
            if j-i+1 > size:
                s-=c[i]
                i+=1
            if j-i+1==size:
                mins=min(mins,s)
        return sum(c)-mins