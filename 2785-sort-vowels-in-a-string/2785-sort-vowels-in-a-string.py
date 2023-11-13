class Solution:
    def sortVowels(self, s: str) -> str:
        vow = []
        pos = []
        
        for i, ch in enumerate(s):
            if ch.lower() in {'a', 'e', 'i', 'o', 'u'}:
                vow.append(ch)
                pos.append(i)
        
        vow.sort()
        answer = list(s)
        
        for i, v in zip(pos, vow):
            answer[i] = v
        
        return ''.join(answer)