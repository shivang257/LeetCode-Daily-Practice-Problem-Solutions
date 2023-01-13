class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        end = float('-inf')
        cnt = 0
        for pair in pairs:
            if end < pair[0]:
                end = pair[1]
                cnt += 1
        return cnt