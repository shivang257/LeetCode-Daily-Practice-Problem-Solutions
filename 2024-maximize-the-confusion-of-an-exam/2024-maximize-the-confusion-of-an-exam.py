class Solution:
    def maxConsecutiveAnswers(self, answer: str, k: int) -> int:
        count=Counter()
        left,ans=0,0
        for right in range(len(answer)):
            count[answer[right]]+=1
            ans=max(ans,count[answer[right]])
            if right-left+1 > k+ans:
                count[answer[left]]-=1
                left+=1
        return len(answer)-left