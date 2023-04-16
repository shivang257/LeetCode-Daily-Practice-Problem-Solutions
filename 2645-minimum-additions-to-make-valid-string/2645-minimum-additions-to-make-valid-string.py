class Solution:
    def addMinimum(self, word: str) -> int:
        k, prev = 0, 'z'
        for c in word:
            k += c <= prev
            prev = c
        return k * 3 - len(word)