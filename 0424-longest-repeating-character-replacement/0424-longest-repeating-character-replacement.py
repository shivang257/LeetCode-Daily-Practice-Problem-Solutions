class Solution: 
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        freq=defaultdict(int)
        ans=0
        for r in range(len(s)):
            freq[s[r]]+=1
            curr=r-l+1
            if curr-max(freq.values())>k:
                freq[s[l]]-=1
                l+=1
            else:
                ans=max(ans,curr)
        return ans