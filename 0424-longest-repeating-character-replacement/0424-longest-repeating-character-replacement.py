class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freqdict = defaultdict(int)
        result = 0
        for r in range(len(s)):
            freqdict[s[r]] += 1
            cur_len = r - l + 1
            if cur_len - max(freqdict.values()) > k:
                freqdict[s[l]] -= 1
                l += 1
            else:
                result = max(result, cur_len)
        return result    
    