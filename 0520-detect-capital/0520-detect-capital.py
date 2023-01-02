class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True
        a=word[0]
        b=(word[1:len(word)])
        return a.isupper() and b.islower()