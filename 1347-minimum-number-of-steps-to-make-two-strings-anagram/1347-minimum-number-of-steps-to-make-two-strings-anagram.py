class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt, steps = Counter(s), 0
        for c in t:
            if cnt[c] > 0:
                cnt[c] -= 1
            else:
                steps += 1
        return steps