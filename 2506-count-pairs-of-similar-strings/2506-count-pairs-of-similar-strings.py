class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
            for w in words[i+1:]:
                if set(w)==set(words[i]):
                    count+=1
        return count