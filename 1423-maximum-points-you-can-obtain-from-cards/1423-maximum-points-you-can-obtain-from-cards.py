class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        i=0
        j=n-k
        total=best=sum(cardPoints[j:])
        for l in range(k):
            total+=cardPoints[i]-cardPoints[j]
            best=max(total,best)
            i+=1;j+=1
        return best