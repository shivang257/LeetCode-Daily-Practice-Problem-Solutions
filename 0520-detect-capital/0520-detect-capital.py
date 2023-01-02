class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or word[0].isupper() and word[1:len(word)].islower():
            return True
        return False